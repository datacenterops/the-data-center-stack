# Data Center Stack Industry Taxonomy

The **Data Center Stack Industry Taxonomy** is a structured classification system for organizations operating across the data center ecosystem.

It extends [The Data Center Stack](../README.md) from a six-layer conceptual framework into a taxonomy that can be referenced by people, software, and AI systems.

## Current version

**v0.1.0 — Draft**

This draft is intended for testing and validation before the first stable release.

## Classification hierarchy

`Stack Layer → Industry Group → Industry → Specialty`

The taxonomy classifies organizations by the **data center function they directly perform**, rather than by generic company descriptions, customer types, or marketing language.

## Core taxonomy

The current draft contains **88 core industry definitions** across the six layers:

| Layer | Taxonomy Action | Industries |
|---|---|---:|
| 1 — Foundation | Build | 12 |
| 2 — Infrastructure | Supply | 18 |
| 3 — Deployment | Deploy | 14 |
| 4 — Operations | Operate | 14 |
| 5 — Platform | Abstract | 14 |
| 6 — Workloads | Run | 16 |

The taxonomy also contains **15 Ecosystem Enabler classifications** for organizations such as consulting firms, financial institutions, associations, media, training providers, government organizations, and other participants that support the ecosystem without directly performing a Layer 1–6 function.

## Canonical source

[`industries.yaml`](./industries.yaml) is the authoritative source for the taxonomy.

The YAML file contains:

- Permanent taxonomy IDs
- Layer and industry-group assignments
- Definitions
- Inclusion criteria
- Exclusion criteria
- Common specialties
- Classification keywords
- Ecosystem Enabler definitions
- Classification rules

## Machine-readable formats

| File | Purpose |
|---|---|
| [`industries.yaml`](./industries.yaml) | Canonical taxonomy source |
| [`taxonomy.json`](./taxonomy.json) | JSON derivative for applications, APIs, and AI workflows |
| [`industries.csv`](./industries.csv) | Flat table for Excel, BI tools, and data analysis |
| [`AI_CLASSIFICATION_GUIDE.md`](./AI_CLASSIFICATION_GUIDE.md) | Instructions for AI-assisted company classification |

The JSON and CSV files should be generated from the YAML source. They should not be edited independently.

## Classification principles

1. **Classify by function.** Determine what the organization actually does within the data center ecosystem.
2. **Select a primary industry.** Choose the industry that best represents the organization's principal data center function.
3. **Use secondary classifications sparingly.** Add another industry or layer only when the organization directly performs that function.
4. **Do not classify by customer relationship.** Selling to a data center operator does not make a company an Operations company.
5. **Use specialties for precision.** A specialty provides detail without creating unnecessary industry categories.
6. **Keep Ecosystem Enablers outside Layers 1–6.** Finance, consulting, media, associations, education, and similar functions support the Stack but are not core Stack layers.
7. **Do not guess.** If there is not enough evidence to classify an organization, use `Research Required`.

## Example

```yaml
company: DatacenterOps
relationship_to_stack: Stack Participant
primary_industry_id: DCS-L3-INS-001
primary_industry: Rack & Stack / Equipment Installation
primary_layer: 3
primary_layer_name: Deployment
secondary_industry_ids:
  - DCS-L3-LOG-001
  - DCS-L3-LCY-001
  - DCS-L3-LCY-003
  - DCS-L4-HND-001
specialties:
  - rack and stack
  - infrastructure deployment
  - data center logistics
  - migration and relocation
  - decommissioning
  - smart hands
confidence: High
```

See [`../examples/company-classifications.yaml`](../examples/company-classifications.yaml) for additional examples.

## Status and contributions

The taxonomy is currently a draft. Definitions, boundaries, and categories should be tested against real company datasets before the first stable release.

When proposing a change, explain:

- Which taxonomy ID is affected
- What problem the current definition creates
- A real company or market example demonstrating the issue
- Whether the change affects an industry, specialty, inclusion, exclusion, or layer assignment

## License

The Data Center Stack Industry Taxonomy is licensed under **Creative Commons Attribution 4.0 International (CC BY 4.0)**.
