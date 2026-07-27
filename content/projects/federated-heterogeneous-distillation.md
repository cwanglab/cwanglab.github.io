---
title: "Federated heterogeneous distillation"
summary: "Collaborative learning across institutions and devices with different local model architectures."
status: "Published"
period: "2021"
research_area: "Heterogeneous intelligence"
order: 30
featured: true
doi: "https://doi.org/10.1109/TII.2020.3007407"
arxiv: ""
code: ""
data: ""
project_url: ""
oa_url: ""
image: ""
---

Collaborative learning usually assumes that every participant trains the same model architecture and can exchange weight updates. In practice, institutions and edge devices run different models on different hardware, and many settings — hospitals among them — cannot centralise their source data. This project studies how knowledge can still be exchanged under those conditions by connecting federated learning with knowledge distillation.

The work, published in *IEEE Transactions on Industrial Informatics*, introduces an industrial cyber-physical systems-based cloud IoT edge framework for federated heterogeneous distillation. Instead of sharing model parameters, participating sites exchange distilled knowledge, so a cloud model and heterogeneous local models with different architectures can teach and learn from one another. Knowledge flows in both directions — cloud to edge and edge to cloud — allowing differently structured systems to contribute and receive useful representations while raw data remain under local governance.

This line of research is a foundation of the group's broader heterogeneous intelligence programme: the aim is not to force every collaborator onto identical infrastructure, but to make collaboration possible across genuine differences in data distribution, model design and computing resource. The same principle now carries through to our work on terminal intelligence, where distilled and parameter-efficient models must operate within the fixed budgets of clinical and robotic endpoints.
