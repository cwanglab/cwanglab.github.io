---
title: "Trustworthy medical AI"
summary: "A model that works on one scanner can fail on the next. We build medical imaging methods that stay reliable across scanners, hospitals and patient groups — for clinicians and population researchers who need measurements they can trust, from UK Biobank-scale studies to point-of-care use."
description: "Trustworthy medical imaging AI that stays reliable across scanners, hospitals and patient groups, from population-scale MRI studies to point-of-care use."
order: 30
diagram: "/images/diagrams/dir-medical-ai.svg"
diagram_alt: "Four-step pipeline: whole-body MRI from UK Biobank, deep-learning measurement of four skeletal sites, phenome-wide and genome-wide association, clinical insight."
diagram_caption: "Schematic. The measurement-to-association pipeline: whole-body MRI, deep-learning measurement at four skeletal sites, PheWAS and GWAS meta-analyses, clinical insight."
image: "/images/research/bone-marrow-measurement.png"
image_size: "wide"
image_alt: "Deep-learning measurement of bone marrow fat fraction in four skeletal regions of UK Biobank MRI, across two participant batches."
image_caption: "Deep-learning segmentation of spine, femoral head, total hip and femoral diaphysis in UK Biobank MRI. The pipeline ran over two imaging batches comprising 50,226 participants; the batch figures shown are the 48,608 retained after sample quality control."
image_source_label: "Xu et al., Nature Communications"
image_source_url: "https://doi.org/10.1038/s41467-024-55422-4"
image_position: "center"
---

We work with MRI, CT, PET and related clinical data on problems including segmentation, registration, image synthesis and quantitative phenotyping. The methodological question is how to learn from differences between scanners, protocols, sites and patient populations without treating those differences as incidental noise.

## Research questions

- Can imaging measurements remain reliable across scanners, protocols, centres and patient groups?
- How can image-derived phenotypes be connected to clinical and genetic evidence?
- What validation is required before a model is useful in a clinical workflow?

## Methods

We develop segmentation, registration, multimodal fusion, image synthesis and quantitative phenotyping methods. Clinical data governance, reproducibility, subgroup analysis and external validation are considered alongside model performance.

## Representative work

- [Deep learning and genome-wide association meta-analyses of bone marrow adiposity in the UK Biobank](/publications/bma-genetics-2025/) (Nature Communications, 2025)
- [Clinical implications of bone marrow adiposity identified by phenome-wide association and Mendelian randomization in the UK Biobank](/publications/bma-clinical-2025/) (Nature Communications, 2025)
