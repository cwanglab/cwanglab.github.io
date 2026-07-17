---
title: "Terminal intelligence"
summary: "Efficient, adaptable and real-time intelligence for clinical, robotic and embedded terminals with fixed resource budgets."
order: 20
image: "/images/research/selora-adaptation.png"
image_alt: "SeLoRA progressively expands low-rank adaptation capacity using a Fisher-information criterion."
image_caption: "SeLoRA starts from a minimal low-rank adaptor and expands capacity only when the Fisher-information criterion indicates that more rank is needed."
image_source_label: "Mao et al., SeLoRA"
image_source_url: "https://arxiv.org/abs/2408.07196"
image_position: "center"
---

Terminal intelligence concerns the point at which a model must sense, decide or assist in the real world. Large models are useful research tools, but many clinical and robotic terminals operate on fixed hardware and within strict response times. We investigate parameter-efficient adaptation, model compression and data-efficient learning so that capability can be transferred from large training environments to practical endpoints.

## Research questions

- Which parts of a large model need to adapt for a specialised terminal task?
- How can memory, trainable parameters and latency be reduced without discarding useful capability?
- When should inference remain local rather than depend on a cloud connection?

## Methods

We study parameter-efficient fine-tuning, adaptive low-rank models, model compression, teacher-student learning and real-time inference. Terminal constraints are treated as part of the learning problem rather than an engineering step after training.

## Representative work

- [SeLoRA: self-expanding low-rank adaptation for medical image synthesis](https://doi.org/10.1016/j.eswa.2026.131569) · [arXiv](https://arxiv.org/abs/2408.07196) · [project page](https://yuchen20.github.io/SeLoRA.github.io/)
- [Enhancing percutaneous coronary intervention with path planning and vascular segmentation](https://doi.org/10.1016/j.compbiomed.2023.107540)
- Data-efficient segmentation through knowledge transfer from large models
