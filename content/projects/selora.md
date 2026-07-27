---
title: "SeLoRA"
summary: "Self-expanding low-rank adaptation for efficient medical image synthesis."
status: "Published"
period: "2024-2026"
research_area: "Terminal intelligence"
order: 10
featured: true
doi: "https://doi.org/10.1016/j.eswa.2026.131569"
arxiv: "https://arxiv.org/abs/2408.07196"
code: "https://github.com/Yuchen20/SeLoRA"
data: ""
project_url: "https://yuchen20.github.io/SeLoRA.github.io/"
image: ""
---

SeLoRA studies how a large latent diffusion model can be adapted to a specialised medical image synthesis task without retraining the full network. Standard low-rank adaptation (LoRA) assigns the same rank to every adapted layer, which treats all weight matrices as equally important. SeLoRA instead starts from a minimal adaptor and expands rank selectively during training: at regular intervals it evaluates a Fisher-information criterion and adds capacity only to the layers where the criterion indicates it is most useful.

The result is a practical answer to a terminal-intelligence question: how much of a large model actually needs to change for a specialised task? In experiments on chest X-ray synthesis datasets, including the small Montgomery County set, SeLoRA matched or exceeded the image quality of vanilla LoRA and other adaptive variants while using roughly half the total rank. The learnt rank allocation is itself interpretable — capacity concentrates on the query and key projections of the cross-attention layers, where text conditioning and image features meet.

The work was published in *Expert Systems with Applications* (volume 314, June 2026). The paper, preprint, training code and a project page with synthesised examples are publicly available through the links on this page. The method is relevant wherever a large pretrained model must be adapted under tight parameter, memory or data budgets, such as clinical imaging terminals.
