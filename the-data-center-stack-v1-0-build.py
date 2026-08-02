#!/usr/bin/env python3
"""Build all Data Center Stack deliverables from the HTML source."""
from playwright.sync_api import sync_playwright
from PIL import Image
import pathlib, os, sys

SRC  = 'data-center-stack.html'
NAME = 'the-data-center-stack-v1-0'
OUT  = '/mnt/user-data/outputs'
url  = pathlib.Path(SRC).resolve().as_uri()

with sync_playwright() as p:
    b  = p.chromium.launch()
    pg = b.new_page(viewport={'width':1750,'height':1200}, device_scale_factor=2)
    pg.goto(url); pg.wait_for_timeout(2500)

    issues = pg.evaluate("""()=>{const o=[];
      document.querySelectorAll('.cell-fn li').forEach(li=>{const lh=parseFloat(getComputedStyle(li).lineHeight);
        if(li.getBoundingClientRect().height>lh*1.4) o.push('BULLET WRAP: '+li.textContent.trim());});
      document.querySelectorAll('.cell-desc p').forEach(pp=>{const lh=parseFloat(getComputedStyle(pp).lineHeight);
        const n=Math.round(pp.getBoundingClientRect().height/lh);
        if(n>3) o.push('DESC '+n+' lines: '+pp.textContent.slice(0,45));});
      document.querySelectorAll('.note').forEach((n,i)=>{
        if(n.scrollHeight>n.clientHeight+2) o.push('NOTE '+(i+1)+' overflow');});
      return o;}""")
    print('layout check:', issues if issues else 'clean')

    sheet = pg.query_selector('.sheet')
    sheet.screenshot(path='_raw.png')

    # PDF sized to the sheet's exact CSS dimensions -> single page, no margins, live text
    box = pg.evaluate("()=>{const r=document.querySelector('.sheet').getBoundingClientRect();"
                      "return {w:r.width,h:r.height};}")
    pg.emulate_media(media='screen')
    pg.add_style_tag(content='html,body{margin:0!important;padding:0!important;background:#FDFDFD}'
                             '.sheet{break-inside:avoid;page-break-inside:avoid}'
                             '@page{margin:0}')
    pg.pdf(path=f'{OUT}/{NAME}.pdf',
           width=f"{box['w']+2}px", height=f"{box['h']+6}px",
           print_background=True, margin={'top':'0','bottom':'0','left':'0','right':'0'})
    b.close()

src  = Image.open('_raw.png').convert('RGB'); W,H = src.size

# LinkedIn: pad to exactly 4:5 so nothing crops in feed
tw   = int(round(H*0.8)); pad = (tw-W)//2
canv = Image.new('RGB',(tw,H),(253,253,253)); canv.paste(src,(pad,0))
canv.resize((2048,2560), Image.LANCZOS).save(f'{OUT}/{NAME}-linkedin.png', optimize=True)

# Full resolution, native ratio
src.save(f'{OUT}/{NAME}.png', optimize=True)
os.system(f'cp {SRC} {OUT}/{NAME}.html')
os.remove('_raw.png')

# enforce the naming convention: lowercase, dashes, no spaces or underscores
import re
BAD = re.compile(r'[A-Z_ ]')
print(f"\nnative {W}x{H}  ratio {W/H:.3f}  ->  4:5 pad {pad}px/side\n")
for f in sorted(os.listdir(OUT)):
    flag = 'BAD NAME' if (BAD.search(f) or not f.startswith(NAME)) else 'ok'
    print(f'  {f:46s} {os.path.getsize(OUT+"/"+f)/1e6:5.2f} MB   {flag}')
