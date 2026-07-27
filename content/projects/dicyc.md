---
title: "DiCyc"
summary: "Deformation-invariant cross-domain information fusion for unpaired medical image synthesis."
status: "Published"
period: "2018-2021"
research_area: "Heterogeneous intelligence"
order: 40
featured: false
doi: "https://doi.org/10.1016/j.inffus.2020.10.015"
arxiv: "https://arxiv.org/abs/1808.03944"
code: ""
data: ""
project_url: ""
oa_url: "https://pmc.ncbi.nlm.nih.gov/articles/PMC7763495/"
image: ""
---

DiCyc addresses a problem that appears whenever medical images are synthesised across domains: the source and target images usually differ not only in appearance but also in geometry. Cycle-consistent GANs handle unpaired training data well, but a standard CycleGAN generator can absorb domain-specific nonlinear deformations into the synthesised image. For downstream applications that depend on spatial alignment — for example generating pseudo-CT for PET-MR attenuation correction — that residual deformation makes the synthesis unreliable.

The method separates deformation from appearance translation. Deformation is parameterised globally with thin-plate splines and learned locally through modified deformable convolutional layers, while new cycle-consistency losses discourage the generator from encoding domain-specific warps. The model was evaluated on multi-sequence brain MR data and on multi-modality abdominal CT-MR data, where it produced synthesised images that stayed aligned with the source domain while preserving signal quality, and it remained comparable to CycleGAN when the domains could be aligned by simple affine transforms.

The work was published in *Information Fusion* in 2021, building on a 2018 preprint. The published version and the preprint are openly accessible through the links on this page. DiCyc remains a reference point in the group's work on cross-domain learning between heterogeneous imaging data.
