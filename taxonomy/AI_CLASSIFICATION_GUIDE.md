# AI Classification Guide

Use `industries.yaml` as the authoritative source when classifying organizations with The Data Center Stack Industry Taxonomy.

## Required process

1. Identify the organization and verify what it actually does in the data center ecosystem.
2. Determine whether it is a:
   - `Stack Participant`
   - `Ecosystem Enabler`
   - `Stack Consumer`
   - `Research Required`
3. For a Stack Participant, compare its functions to the definitions in `industries.yaml`.
4. Select one `primary_industry_id` whenever possible.
5. Use the industry's `primary_layer` as the organization's primary Stack layer.
6. Add secondary industries only when the organization directly performs a separate material function.
7. Use `common_specialties` to describe narrower capabilities without inventing new industries.
8. Use `includes`, `excludes`, and `keywords` to resolve close classifications.
9. Do not assign a layer because the organization sells to, buys from, depends on, or is used by that layer.
10. If evidence is insufficient or contradictory, return `Research Required` rather than guessing.

## Evidence

Classification should be based on reliable evidence such as:

- Official company website
- Product or services pages
- Annual reports or regulatory filings
- Official company descriptions
- Credible industry sources

Do not classify solely from a company name when the business function is unclear.

## Confidence

Use:

- `High` — identity and data center function are clear
- `Medium` — classification is likely but the company spans categories or needs additional validation
- `Low` — evidence is weak or classification is ambiguous
- `Research Required` — insufficient evidence to select a taxonomy classification

## Recommended output

```json
{
  "company": "DatacenterOps",
  "relationship_to_stack": "Stack Participant",
  "primary_industry_id": "DCS-L3-INS-001",
  "primary_industry": "Rack & Stack / Equipment Installation",
  "primary_layer": 3,
  "primary_layer_name": "Deployment",
  "secondary_industry_ids": [
    "DCS-L3-LOG-001",
    "DCS-L3-LCY-001",
    "DCS-L3-LCY-003",
    "DCS-L4-HND-001"
  ],
  "specialties": [
    "rack and stack",
    "infrastructure deployment",
    "data center logistics",
    "migration and relocation",
    "decommissioning",
    "smart hands"
  ],
  "confidence": "High",
  "reason": "Its primary data center function is deploying IT infrastructure inside data centers, with additional material functions in logistics, migrations, decommissioning and smart hands."
}
```

## Multi-function organizations

Large organizations may perform functions across multiple layers. Do not classify every business unit automatically.

Ask:

> Where does this organization create its principal data center value?

Use that answer for the primary classification. Add secondary classifications only when the additional function is material to the organization being analyzed.

## Ecosystem Enablers

Do not force organizations such as consulting firms, investors, insurers, law firms, media companies, associations, training providers, or economic-development organizations into Layers 1–6.

Use the `ecosystem_enablers` section of `industries.yaml`.

## Stack Consumers

An organization can operate significant data center infrastructure without being a supplier to the data center ecosystem.

For example, a bank operating its own data centers may be a `Stack Consumer` with financial workloads rather than a data center industry supplier.

## Taxonomy IDs

Always return taxonomy IDs along with human-readable names. Names can evolve over time; IDs are intended to remain stable.
