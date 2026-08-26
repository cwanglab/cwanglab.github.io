---
title: "Heterogeneous intelligence"
summary: "Hospitals and research partners often cannot pool data or run identical hardware. We build federated learning and knowledge-distillation methods that let AI models learn across institutions, model architectures and devices — for clinical networks that must keep source data under local governance."
description: "Federated learning and knowledge transfer across institutions, model architectures and devices, without moving source data."
order: 10
diagram: "/images/diagrams/dir-heterogeneous.svg"
diagram_alt: "Overview of heterogeneous intelligence: federated learning and knowledge distillation across institutions, model architectures and devices."
diagram_caption: "Schematic. This direction at a glance: models learn across institutions, architectures and devices while source data stay under local governance."
image: "/images/research/dicyc-fig4.jpg"
image_size: "wide"
image_alt: "Brain MR cross-domain synthesis: PD and T2 inputs translated by DiCycleGAN and CycleGAN, beside ground truth and difference maps."
image_caption: "Cross-domain synthesis with deformation-invariant cycle consistency: translating between PD- and T2-weighted brain MR without paired data, shown against ground truth and difference maps."
image_source_label: "Wang et al., arXiv:1808.03944"
image_source_url: "https://arxiv.org/abs/1808.03944"
image_position: "center"
---

Heterogeneous intelligence is the study of learning systems that must operate across differences rather than assuming a uniform dataset, model or device. Hospitals and research partners often cannot pool data and do not operate identical infrastructure. We study federated, distributed and knowledge-distillation methods that allow models to learn across these boundaries while keeping source data under local governance.

## Research questions

- What knowledge can be exchanged when institutions use different model architectures and hardware?
- How should collaboration work when source data remain under local governance?
- How do we evaluate robustness across sites instead of relying on one aggregate test set?

## Methods

Our work combines federated learning, online knowledge distillation, cross-domain synthesis and distributed optimisation. The aim is not to make every participant identical, but to let differently structured systems contribute and receive useful knowledge.

## Representative work

- [DiCyc: GAN-based deformation-invariant cross-domain information fusion for medical image synthesis](/publications/dicyc-2021/) (Information Fusion, 2021)
- [Industrial cyber-physical systems-based cloud IoT edge for federated heterogeneous distillation](https://doi.org/10.1109/TII.2020.3007407) (IEEE Transactions on Industrial Informatics, 2021) · [project page](/projects/federated-heterogeneous-distillation/)
