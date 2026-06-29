---
title: "Research"
description: "Heterogeneous Medical AI across a Cloud–Edge–Terminal framework — population-scale imaging, federated learning, and on-device clinical inference, grounded in five multicentre trials."
---

<p class="eyebrow">FRAMEWORK</p>

## The compute gap

Everyone uses large models; nobody can afford them everywhere. A roughly **15,000× gap in compute** separates the data-centre GPUs that train modern foundation models from the workstations and handheld devices where clinical decisions are actually made. Closing that gap is the central problem of **Heterogeneous Medical AI**: building systems that hold up across four kinds of heterogeneity, and that move capability to wherever the patient is.

<div class="card-grid">
<div class="card">
<h3>Data</h3>
<p>Heterogeneous modalities, sites and scanners — MRI, CT, PET, ultrasound and EHR — with differing protocols, vendors and distributions.</p>
</div>
<div class="card">
<h3>Device</h3>
<p>Compute that ranges across orders of magnitude, from data-centre clusters to hospital workstations to point-of-care endpoints.</p>
</div>
<div class="card">
<h3>Model</h3>
<p>No single architecture serves every setting; capacity must scale down to the endpoint without discarding what large models learned.</p>
</div>
<div class="card">
<h3>Demand</h3>
<p>Clinical needs differ by task and latency budget, from population-scale analytics to sub-second intra-operative inference.</p>
</div>
</div>

We organise this work as a **Cloud–Edge–Terminal** framework, and ground it in nine years of NHS-embedded research and five multicentre clinical trials.

<p class="eyebrow">CLOUD</p>

## Population analytics and cross-domain synthesis

At population scale, the constraint is throughput and consistency, not latency. We build high-throughput pipelines that read tens of thousands of studies, harmonise data across centres and scanners, and recover the causal structure linking imaging phenotypes to disease.

<div class="card-grid">
<div class="card">
<h3>Population-scale imaging pipelines</h3>
<p>High-throughput analysis of UK Biobank whole-body MRI (39,000+ subjects), turning raw volumes into quantitative phenotypes at cohort scale.</p>
<p style="font-size:0.8rem;color:var(--ink-muted);"><em>Nature Communications ×2 (2025) · Computational &amp; Structural Biotechnology Journal (2024)</em></p>
</div>
<div class="card">
<h3>Cross-modal synthesis &amp; harmonisation</h3>
<p>Deformation-invariant cross-domain synthesis that bridges modalities and reconciles multi-centre acquisition differences without paired data.</p>
<p style="font-size:0.8rem;color:var(--ink-muted);"><em>Information Fusion (2021) · Medical Image Analysis (2021)</em></p>
</div>
<div class="card">
<h3>Causal phenotype discovery</h3>
<p>Linking deep-learned imaging phenotypes to clinical outcomes through PheWAS and Mendelian randomisation to separate association from cause.</p>
<p style="font-size:0.8rem;color:var(--ink-muted);"><em>Nature Communications (2025)</em></p>
</div>
</div>

<p class="eyebrow">EDGE</p>

## Federated and privacy-preserving learning

Hospitals hold complementary data but cannot pool it, and rarely run the same hardware. We develop learning that crosses institutional and device boundaries — sharing knowledge, not patient data — and the fog–cloud architectures that make distributed inference robust.

<div class="card-grid">
<div class="card">
<h3>Heterogeneous federated distillation</h3>
<p>Knowledge distillation that lets hospitals with different model architectures and hardware learn together, without any patient data leaving its site.</p>
<p style="font-size:0.8rem;color:var(--ink-muted);"><em>IEEE Transactions on Medical Imaging (2020)</em></p>
</div>
<div class="card">
<h3>Fog–cloud cyber-physical systems</h3>
<p>Distributed architectures for industrial cyber-physical and IoT settings, including semi-supervised learning that tolerates sparse, noisy labels at the edge.</p>
<p style="font-size:0.8rem;color:var(--ink-muted);"><em>IEEE Transactions on Industrial Informatics ×2 (2020)</em></p>
</div>
</div>

<p class="eyebrow">TERMINAL</p>

## Lightweight inference and real-time clinical decision

At the point of care the budget is fixed: a single workstation, a few hundred milliseconds, no cloud. We compress foundation-model capability into endpoint-sized models and deploy them for live intervention and screening.

<div class="card-grid">
<div class="card">
<h3>Parameter-efficient adaptation</h3>
<p>SeLoRA adapts a foundation model by training 8.5M of 850M parameters (~1%), recovering full-tuning quality at a fraction of the memory and compute.</p>
<p style="font-size:0.8rem;color:var(--ink-muted);"><em>Expert Systems with Applications (2026)</em></p>
</div>
<div class="card">
<h3>Point-of-care intervention AI</h3>
<p>Sub-second path planning for coronary intervention, running intra-operatively on the procedure-room workstation rather than a remote server.</p>
<p style="font-size:0.8rem;color:var(--ink-muted);"><em>Computers in Biology &amp; Medicine (2023)</em></p>
</div>
<div class="card">
<h3>On-device diagnostic screening</h3>
<p>Large-scale screening for immunodeficiencies, validated multi-centre and blinded against expert-level performance.</p>
<p style="font-size:0.8rem;color:var(--ink-muted);"><em>Communications Medicine (2023)</em></p>
</div>
</div>

This progression follows a **natural evolution** rather than a chase for trends: each method solves a problem the previous one exposed — from image registration in MA3RS, to multimodal fusion (DiCyc), to federated distillation, to parameter-efficient adaptation (SeLoRA).

<p class="eyebrow">CLINICAL TRANSLATION</p>

## Five multicentre trials

The methods above are grounded in AI work for five multicentre cardiovascular trials, with combined trial funding exceeding **£5M**. The trials are where heterogeneity stops being an abstraction: real scanners, real vendors, real patients.

<div class="card-grid">
<div class="card">
<h3>SCOT-HEART</h3>
<p>Coronary CTA screening across 12 centres and 4,146 patients. AI role: automated plaque quantification, cross-device robustness across 12 scanners, and risk stratification.</p>
<p style="font-size:0.8rem;color:var(--ink-muted);"><em>CSO £553K · Circulation (2020)</em></p>
</div>
<div class="card">
<h3>MA3RS</h3>
<p>Abdominal aortic aneurysm imaging with USPIO-MRI. AI role: multi-modality registration of MRI, PET and CT, and 3D aneurysm classification.</p>
<p style="font-size:0.8rem;color:var(--ink-muted);"><em>BHF £1.8M · Circulation (2017); J. Vascular Surgery (2017)</em></p>
</div>
<div class="card">
<h3>PREFFIR</h3>
<p>Coronary plaque rupture imaging with <sup>18</sup>F-NaF PET. AI role: PET/CT motion compensation and uptake quantification.</p>
<p style="font-size:0.8rem;color:var(--ink-muted);"><em>Wellcome Trust £2.5M</em></p>
</div>
<div class="card">
<h3>DIAMOND</h3>
<p>Aortic stenosis trial at Edinburgh. AI role: cardiac MR T1 and ECV mapping with cross-vendor harmonisation.</p>
<p style="font-size:0.8rem;color:var(--ink-muted);"><em>Edinburgh BHF · JACC: Cardiovascular Imaging ×2</em></p>
</div>
<div class="card">
<h3>SALTIRE II</h3>
<p>Aortic valve calcification trial at Edinburgh. AI role: automated calcification scoring.</p>
<p style="font-size:0.8rem;color:var(--ink-muted);"><em>Edinburgh BHF</em></p>
</div>
</div>

<p class="eyebrow">CAPABILITIES</p>

## Methods and capabilities

Across the three layers, the group works with:

- Multi-modality fusion across MRI, CT, PET, ultrasound and EHR
- Longitudinal data synthesis and disentangled representation learning
- Causal and explainable AI
- Federated and privacy-preserving learning
- Foundation-model adaptation (PEFT / LoRA) and model compression
- Cross-domain synthesis with GANs, diffusion and flow models
- Semi-supervised and active learning under label scarcity
- Population-scale biobank analytics and high-throughput pipelines
- On-device, real-time inference for point-of-care deployment
- An AI-driven drug-discovery pipeline (with Pfizer) and micro/nano-robot control

[Publications and Google Scholar →](/publications/)
