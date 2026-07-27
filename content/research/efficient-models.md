---
title: "Terminal intelligence"
summary: "Scanners, surgical systems and robots run on fixed hardware with strict time budgets. We make large models adapt to specialised clinical and robotic tasks with minimal trainable parameters and latency — for teams deploying AI on real terminals, not just in the cloud."
description: "Parameter-efficient adaptation and compression that puts large-model capability onto clinical and robotic terminals with fixed resource budgets."
order: 20
diagram: "/images/diagrams/dir-terminal.svg"
diagram_alt: "Overview of terminal intelligence: parameter-efficient adaptation and compression that bring large-model capability to fixed clinical and robotic terminals."
diagram_caption: "Schematic. This direction at a glance: large-model capability, adapted and compressed to run on real clinical and robotic terminals."
---

Terminal intelligence concerns the point at which a model must sense, decide or assist in the real world. Large models are useful research tools, but many clinical and robotic terminals operate on fixed hardware and within strict response times. We investigate parameter-efficient adaptation, model compression and data-efficient learning so that capability can be transferred from large training environments to practical endpoints.

## Research questions

- Which parts of a large model need to adapt for a specialised terminal task?
- How can memory, trainable parameters and latency be reduced without discarding useful capability?
- When should inference remain local rather than depend on a cloud connection?

## Methods

We study parameter-efficient fine-tuning, adaptive low-rank models, model compression, teacher-student learning and real-time inference. Terminal constraints are treated as part of the learning problem rather than an engineering step after training.

## Representative work

- [SeLoRA: self-expanding LoRA for high-quality and efficient medical image synthesis](/publications/selora-2026/) (Expert Systems with Applications, 2026) · [project page](/projects/selora/)
- [Enhancing percutaneous coronary intervention with heuristic path planning and deep-learning-based vascular segmentation](/publications/pci-path-planning-2023/) (Computers in Biology and Medicine, 2023)
