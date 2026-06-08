---
layout: modern
title: "Week 23 — 2026-06-01 – 2026-06-07"
week: 23
paper_count: 40
news_count: 88
repo_count: 14
permalink: /weekly/23/
---

<div class="weekly-stats-bar">
  <span class="weekly-stat"><strong>40</strong> papers</span>
  <span class="weekly-stat-sep">·</span>
  <span class="weekly-stat"><strong>88</strong> news</span>
  <span class="weekly-stat-sep">·</span>
  <span class="weekly-stat"><strong>14</strong> repos</span>
  <span class="weekly-stat-sep">·</span>
  <span class="weekly-stat">Week <strong>23</strong></span>
</div>

<div class="weekly-narrative">
  <p>This week in AI and tech underscored a growing emphasis on structured reasoning, ethical transparency, and agentic systems, with key papers advancing uncertainty-aware reinforcement learning for autonomous driving, privacy-preserving LLM evaluation frameworks, and memory-centric scientific research agents. NVIDIA’s innovations in agentic AI infrastructure, including the Vera CPU and DSX OS, highlighted the push toward scalable, secure AI factories, while security concerns emerged around ChatGPT’s integration with Google Sheets, exposing data exfiltration risks. Community discussions centered on disentangling evolution capabilities in self-evolving models, the challenges of physically grounded world models, and debates over the practicality of synthetic deception in LLMs, reflecting tensions between technical progress and ethical accountability. Meanwhile, open-source projects like AutoSci and PhyDrawGen signaled a shift toward tools that bridge theoretical advancements with real-world applications, even as low-star repositories hinted at fragmented community engagement in niche areas like agentic RAG and harness engineering.</p>
</div>

<hr>

<h2 id="papers">Research Highlights</h2>

<h3 id="papers-by-area">By Research Area</h3>
<p class="section-desc">Top papers per ArXiv subject category, ranked by relevance.</p>

<h4>AI Safety</h4>
<div class="weekly-paper-list">

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#1</span>
    <span class="rel-dots" aria-label="Relevance: 5 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ml" title="Machine Learning (cs.LG)">Machine Learning (cs.LG)</span><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span></span>
    <span class="paper-date">1 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2605.30381">When LLMs Learn to Be Consistently Wrong: A Multi-Model Study of Linear Representations of Synthetic Deception</a>
  <p class="weekly-paper-contribution">This study demonstrates that synthetic deception in LLMs can be systematically analyzed through linear representations, revealing domain-invariant dishonesty patterns achievable via minimal fine-tuning.</p>
</div>

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#2</span>
    <span class="rel-dots" aria-label="Relevance: 4 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span></span>
    <span class="paper-date">1 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2605.30803">PReMISE: Policy Rubrics as Measurement Specifications for LLM Judges</a>
  <p class="weekly-paper-contribution">PReMISE introduces a framework for discovering policy-level rubrics and auditing their reliability, preference fit, and robustness under LLM judges, with repair operations that improve judge accuracy and reduce exploitability.</p>
</div>

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#3</span>
    <span class="rel-dots" aria-label="Relevance: 4 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span></span>
    <span class="paper-date">1 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2605.30838">COMPASS: Cognitive MCTS-Guided Process Alignment for Safe Search Agents</a>
  <p class="weekly-paper-contribution">COMPASS introduces a novel framework for aligning search agents with safety constraints by addressing retrieval-induced safety degradation through cognitive tree exploration and introspective alignment.</p>
</div>

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#4</span>
    <span class="rel-dots" aria-label="Relevance: 3 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot"></span><span class="rel-dot"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span><span class="cat-tag cat-ai" title="Multiagent Systems (cs.MA)">Multiagent Systems (cs.MA)</span></span>
    <span class="paper-date">1 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2605.30680">Healthcare Mechanisms from Policy-as-Code Search under Strategic Provider Response</a>
  <p class="weekly-paper-contribution">This paper introduces a novel approach to healthcare mechanism design by integrating program synthesis with strategic provider behavior modeling, enabling evaluation of mechanisms through equilibrium outcomes rather than fixed responses.</p>
</div>

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#5</span>
    <span class="rel-dots" aria-label="Relevance: 3 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot"></span><span class="rel-dot"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span><span class="cat-tag cat-nlp" title="Computation and Language (cs.CL)">Computation and Language (cs.CL)</span><span class="cat-tag cat-ml" title="Machine Learning (cs.LG)">Machine Learning (cs.LG)</span></span>
    <span class="paper-date">1 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2605.31021">A Persona-Based Evaluation Framework for Pluralistic Alignment in Generative AI</a>
  <p class="weekly-paper-contribution">Introduces a persona-based evaluation framework for generative AI that captures cultural, demographic, and contextual variability through synthetic cognitive profiles, replacing monolithic benchmarks with pluralistic, perspective-dependent assessment.</p>
</div>

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#6</span>
    <span class="rel-dots" aria-label="Relevance: 3 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot"></span><span class="rel-dot"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span></span>
    <span class="paper-date">1 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2605.31254">Formalizing and falsifying causal pathways of rare events</a>
  <p class="weekly-paper-contribution">This paper formally defines causal pathways for rare events and establishes testable implications that depend on causal abstractions rather than full system models.</p>
</div>

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#7</span>
    <span class="rel-dots" aria-label="Relevance: 3 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot"></span><span class="rel-dot"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span></span>
    <span class="paper-date">1 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2605.31581">Choosing the Lens: Strategic Perspective Activation in Context-Dependent Argumentation</a>
  <p class="weekly-paper-contribution">Introduces context-dependent argumentation frameworks (CDAFs) and the ACTIVATION-MANIPULATION decision problem, extending Dung&#x27;s theory to model strategic control over argument evaluation through context-specific defeat functions.</p>
</div>

</div>

<h4>Agentic AI</h4>
<div class="weekly-paper-list">

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#1</span>
    <span class="rel-dots" aria-label="Relevance: 5 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span></span>
    <span class="paper-date">1 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2605.30738">MAVEN: Improving Generalization in Agentic Tool Calling</a>
  <p class="weekly-paper-contribution">MAVEN introduces a lightweight symbolic reasoning framework to enhance generalization in agentic tool calling, demonstrating significant accuracy improvements on multi-step reasoning benchmarks without additional training.</p>
</div>

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#2</span>
    <span class="rel-dots" aria-label="Relevance: 5 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span></span>
    <span class="paper-date">1 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2605.31468">AutoSci: A Memory-Centric Agentic System for the Full Scientific Research Lifecycle</a>
  <p class="weekly-paper-contribution">AutoSci introduces a unified, memory-centric agentic system that automates the entire scientific research lifecycle, addressing gaps in existing systems by integrating structured memory, dynamic workflow execution, skill augmentation, and iterative evolution.</p>
</div>

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#3</span>
    <span class="rel-dots" aria-label="Relevance: 4 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span></span>
    <span class="paper-date">1 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2605.30621">Harness Updating Is Not Harness Benefit: Disentangling Evolution Capabilities in Self-Evolving LLM Agents</a>
  <p class="weekly-paper-contribution">This paper disentangles two distinct capabilities in self-evolving LLM agents—harness-updating and harness-benefit—revealing that base model capability does not predict effectiveness in harness self-evolution.</p>
</div>

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#4</span>
    <span class="rel-dots" aria-label="Relevance: 4 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span></span>
    <span class="paper-date">1 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2605.30785">Learning Agent-Compatible Context Management for Long-Horizon Tasks</a>
  <p class="weekly-paper-contribution">Introduces AdaCoM, an external context management system that improves long-horizon task performance for frozen agents without retraining, revealing a fidelity-reliability trade-off in context management strategies.</p>
</div>

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#5</span>
    <span class="rel-dots" aria-label="Relevance: 4 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span><span class="cat-tag cat-nlp" title="Computation and Language (cs.CL)">Computation and Language (cs.CL)</span><span class="cat-tag cat-ml" title="Machine Learning (cs.LG)">Machine Learning (cs.LG)</span></span>
    <span class="paper-date">1 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2605.31264">COLLEAGUE.SKILL: Automated AI Skill Generation via Expert Knowledge Distillation</a>
  <p class="weekly-paper-contribution">COLLEAGUE.SKILL introduces an end-to-end system for distilling heterogeneous expert traces into inspectable, correctable AI skill packages grounded in human expertise and behavior.</p>
</div>

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#6</span>
    <span class="rel-dots" aria-label="Relevance: 4 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span><span class="cat-tag cat-ml" title="Machine Learning (cs.LG)">Machine Learning (cs.LG)</span><span class="cat-tag cat-default" title="stat.ME">stat.ME</span></span>
    <span class="paper-date">1 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2605.31278">Industrializing Prediction-Powered Inference: The GLIDE Library for Reliable GenAI and Agentic Systems Evaluation</a>
  <p class="weekly-paper-contribution">GLIDE introduces an open-source Python library that unifies state-of-the-art prediction-powered inference (PPI) estimators and samplers for reliable evaluation of agentic systems, reducing reliance on costly human annotations or biased LLM judgments.</p>
</div>

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#7</span>
    <span class="rel-dots" aria-label="Relevance: 4 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span></span>
    <span class="paper-date">1 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2605.31365">Learning to Adapt: Self-Improving Web Agent via Cognitive-Aware Exploration</a>
  <p class="weekly-paper-contribution">SCALE introduces a self-improving web agent framework that autonomously expands cognitive boundaries through adversarial roles and graph-based exploration, reducing reliance on handcrafted pipelines and expert trajectories.</p>
</div>

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#8</span>
    <span class="rel-dots" aria-label="Relevance: 4 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span></span>
    <span class="paper-date">1 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2605.31370">HypoAgent: An Agentic Framework for Interactive Abductive Hypothesis Generation over Knowledge Graphs</a>
  <p class="weekly-paper-contribution">HypoAgent introduces an agentic framework for interactive abductive hypothesis generation over knowledge graphs, addressing limitations in handling evolving dialogues and providing fine-grained diagnosis.</p>
</div>

</div>

<h4>Computer Vision</h4>
<div class="weekly-paper-list">

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#1</span>
    <span class="rel-dots" aria-label="Relevance: 4 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span><span class="cat-tag cat-physics" title="physics.app-ph">physics.app-ph</span></span>
    <span class="paper-date">1 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2605.30900">BilliardPhys-Bench: Benchmarking Physical Reasoning and Visual Dynamics of Multimodal LLMs</a>
  <p class="weekly-paper-contribution">BilliardPhys-Bench introduces a synthetic benchmark to evaluate physical reasoning and visual dynamics prediction in multimodal large language models (MLLMs) through billiards scenarios.</p>
</div>

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#2</span>
    <span class="rel-dots" aria-label="Relevance: 3 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot"></span><span class="rel-dot"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span><span class="cat-tag cat-ml" title="Machine Learning (cs.LG)">Machine Learning (cs.LG)</span></span>
    <span class="paper-date">1 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2605.31354">Diagnosing Failure Modes of Shared-State Collaboration in Resource-Constrained Visual Agents</a>
  <p class="weekly-paper-contribution">This work identifies critical failure modes in shared-state collaboration for resource-constrained visual agents and introduces CoSee, a framework for diagnosing noise accumulation in multi-step reasoning.</p>
</div>

</div>

<h4>Computing Systems</h4>
<div class="weekly-paper-list">

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#1</span>
    <span class="rel-dots" aria-label="Relevance: 3 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot"></span><span class="rel-dot"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span></span>
    <span class="paper-date">1 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2605.30563">Transforming and Encoding FTS for SAT Solving: What Helps, What Hurts (Extended Version)</a>
  <p class="weekly-paper-contribution">This work introduces multiple SAT encodings for factored tasks and systematically evaluates their effectiveness, along with the impact of task transformations and parallelism on SAT-based planning performance.</p>
</div>

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#2</span>
    <span class="rel-dots" aria-label="Relevance: 3 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot"></span><span class="rel-dot"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ml" title="Machine Learning (cs.LG)">Machine Learning (cs.LG)</span></span>
    <span class="paper-date">1 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2605.30358">QASM-Eval: A Dataset to Train and Evaluate LLMs on OpenQASM-3 Beyond Quantum Circuits</a>
  <p class="weekly-paper-contribution">QASM-Eval is the first comprehensive dataset designed to train and evaluate LLMs on OpenQASM-3 programs, focusing on hardware-facing features beyond quantum circuits.</p>
</div>

</div>

<h4>General</h4>
<div class="weekly-paper-list">

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#1</span>
    <span class="rel-dots" aria-label="Relevance: 4 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span></span>
    <span class="paper-date">1 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2605.31410">FAM-Bench: A Multimodal Benchmark for Condition-Aware Food-as-Medicine Reasoning</a>
  <p class="weekly-paper-contribution">FAM-Bench introduces the first multi-modal benchmark for evaluating condition-aware Food-as-Medicine reasoning, addressing the gap in health-aware decision-making in existing food AI benchmarks.</p>
</div>

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#2</span>
    <span class="rel-dots" aria-label="Relevance: 3 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot"></span><span class="rel-dot"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span></span>
    <span class="paper-date">1 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2605.31031">GraphARC: A Comprehensive Benchmark for Graph-Based Abstract Reasoning</a>
  <p class="weekly-paper-contribution">GraphARC introduces a scalable benchmark for abstract reasoning on graph-structured data, extending the ARC paradigm to evaluate generalization in graph transformations.</p>
</div>

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#3</span>
    <span class="rel-dots" aria-label="Relevance: 3 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot"></span><span class="rel-dot"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ml" title="Machine Learning (cs.LG)">Machine Learning (cs.LG)</span><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span></span>
    <span class="paper-date">1 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2605.30376">Unicorn: Scaling High-Dimensional Time Series Forecasting via Universal Correlation Modeling</a>
  <p class="weekly-paper-contribution">Unicorn introduces a scalable framework for high-dimensional time series forecasting by decoupling correlation modeling from channel identities, enabling cross-domain generalization and few-shot transfer.</p>
</div>

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#4</span>
    <span class="rel-dots" aria-label="Relevance: 2 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot"></span><span class="rel-dot"></span><span class="rel-dot"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span></span>
    <span class="paper-date">1 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2605.30570">Procedural Generation of First Person Shooter Maps using Map-Elites</a>
  <p class="weekly-paper-contribution">This paper introduces novel map representations (Point-Line and Spatial-Layout) and demonstrates their superiority in generating diverse, high-quality FPS maps using MAP-Elites compared to existing representations.</p>
</div>

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#5</span>
    <span class="rel-dots" aria-label="Relevance: 2 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot"></span><span class="rel-dot"></span><span class="rel-dot"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ml" title="Machine Learning (cs.LG)">Machine Learning (cs.LG)</span></span>
    <span class="paper-date">1 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2605.30374">Gait2Hip-60: A Unified Deep Learning Benchmark for Predicting Hip Muscle Forces and Joint Moments from Multi-Cadence Gait Kinematics</a>
  <p class="weekly-paper-contribution">Developed a deep learning benchmark (Gait2Hip-60) for predicting hip muscle forces and joint moments directly from gait kinematics, enabling faster and more clinically applicable alternatives to traditional musculoskeletal simulations.</p>
</div>

</div>

<h4>LLM</h4>
<div class="weekly-paper-list">

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#1</span>
    <span class="rel-dots" aria-label="Relevance: 5 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span></span>
    <span class="paper-date">1 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2605.31167">LLM-FACETS: A Privacy-Preserving Framework for Evaluating LLM Transparency and Accountability</a>
  <p class="weekly-paper-contribution">LLM-FACETS introduces an open-source, privacy-preserving framework for evaluating LLM transparency and accountability, enabling non-technical practitioners to audit models without data transmission or programming expertise.</p>
</div>

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#2</span>
    <span class="rel-dots" aria-label="Relevance: 5 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span></span>
    <span class="paper-date">1 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2605.31492">LinTree: Improving LLM Reasoning with Explicitly Structured Search Histories</a>
  <p class="weekly-paper-contribution">LinTree demonstrates that explicitly structuring search histories with parent pointers improves LLM reasoning performance and efficiency compared to implicit trace representations and heuristic-based search.</p>
</div>

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#3</span>
    <span class="rel-dots" aria-label="Relevance: 4 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span></span>
    <span class="paper-date">1 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2605.30832">SLAT: Segment-Level Adaptive Trimming for Efficient CoT Reasoning</a>
  <p class="weekly-paper-contribution">SLAT introduces a segment-level adaptive trimming framework to enhance the efficiency of chain-of-thought (CoT) reasoning in large language models by addressing structural redundancy without compromising accuracy.</p>
</div>

</div>

<h4>MLOps</h4>
<div class="weekly-paper-list">

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#1</span>
    <span class="rel-dots" aria-label="Relevance: 4 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span><span class="cat-tag cat-nlp" title="Computation and Language (cs.CL)">Computation and Language (cs.CL)</span></span>
    <span class="paper-date">1 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2605.30898">UniScale: Adaptive Unified Inference Scaling via Online Joint Optimization of Model Routing and Test-Time Scaling</a>
  <p class="weekly-paper-contribution">UniScale unifies model routing and test-time scaling into a single optimization framework, overcoming limitations of decoupled approaches and achieving superior quality-cost trade-offs in dynamic inference scenarios.</p>
</div>

</div>

<h4>NLP</h4>
<div class="weekly-paper-list">

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#1</span>
    <span class="rel-dots" aria-label="Relevance: 4 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span><span class="cat-tag cat-cv" title="Computer Vision and Pattern Recognition (cs.CV)">Computer Vision and Pattern Recognition (cs.CV)</span></span>
    <span class="paper-date">1 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2605.30512">PhyDrawGen: Physically Grounded Diagram Generation from Natural Language</a>
  <p class="weekly-paper-contribution">PhyDrawGen addresses systematic errors in physics diagram generation by integrating symbolic physics constraints with visual generation, achieving robust physical accuracy across diverse domains.</p>
</div>

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#2</span>
    <span class="rel-dots" aria-label="Relevance: 4 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span><span class="cat-tag cat-default" title="Databases (cs.DB)">Databases (cs.DB)</span><span class="cat-tag cat-ir" title="Information Retrieval (cs.IR)">Information Retrieval (cs.IR)</span></span>
    <span class="paper-date">1 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2605.31100">Vector Linking via Cross-Model Local Isometric Consistency</a>
  <p class="weekly-paper-contribution">This paper introduces a method for cross-model vector linking using local geometric consistency, enabling accurate correspondences between embedding clouds from different encoders without requiring model access or labels.</p>
</div>

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#3</span>
    <span class="rel-dots" aria-label="Relevance: 3 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot"></span><span class="rel-dot"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span></span>
    <span class="paper-date">1 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2605.30637">EHRBench: An Automated and Reliable EHR-based Benchmark for Clinical Decision Making with LLMs</a>
  <p class="weekly-paper-contribution">EHRBench introduces an automated, EHR-grounded benchmark for evaluating LLMs in clinical decision-making, addressing scalability and reliability gaps in real-world CDM tasks.</p>
</div>

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#4</span>
    <span class="rel-dots" aria-label="Relevance: 3 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot"></span><span class="rel-dot"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span></span>
    <span class="paper-date">1 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2605.30747">Generating Graph-like Rules for Knowledge Graph Reasoning via Diffusion Models</a>
  <p class="weekly-paper-contribution">GRiD introduces a novel framework for discovering graph-like rules in knowledge graphs using diffusion models, addressing limitations of existing methods that overlook complex relational structures and computational challenges.</p>
</div>

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#5</span>
    <span class="rel-dots" aria-label="Relevance: 3 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot"></span><span class="rel-dot"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span></span>
    <span class="paper-date">1 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2605.30861">Distilling LLM Feedback for Lean Theorem Proving</a>
  <p class="weekly-paper-contribution">Introduces Feedback Distillation, a novel training method for reasoning models that improves post-training performance in complex tasks like Lean4 theorem proving by leveraging self-distillation with privileged feedback.</p>
</div>

</div>

<h4>RL</h4>
<div class="weekly-paper-list">

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#1</span>
    <span class="rel-dots" aria-label="Relevance: 5 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span></span>
    <span class="paper-date">1 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2605.30576">Uncertainty-Aware and Temporally Regulated Expert Advice in Reinforcement Learning for Autonomous Driving</a>
  <p class="weekly-paper-contribution">Proposes an uncertainty-aware framework that integrates expert advice with temporally regulated guidance to enhance safe and efficient exploration in reinforcement learning for autonomous driving.</p>
</div>

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#2</span>
    <span class="rel-dots" aria-label="Relevance: 5 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span></span>
    <span class="paper-date">1 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2605.30824">Planner-Centric Reinforcement Learning for Deep Research with Structure-Aware Reward</a>
  <p class="weekly-paper-contribution">DecomposeR introduces a planner-centric framework for deep research tasks using structured reward mechanisms, improving planning and answering capabilities in LLMs.</p>
</div>

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#3</span>
    <span class="rel-dots" aria-label="Relevance: 4 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span></span>
    <span class="paper-date">1 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2605.31308">TraceGraph: Shared Decision Landscapes for Diagnosing and Improving Agent Trajectories</a>
  <p class="weekly-paper-contribution">TraceGraph introduces a graph-based framework to analyze agent trajectories, revealing hidden navigation differences and motivating trap-aware recovery pipelines for improving model performance.</p>
</div>

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#4</span>
    <span class="rel-dots" aria-label="Relevance: 4 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span><span class="cat-tag cat-default" title="Logic in Computer Science (cs.LO)">Logic in Computer Science (cs.LO)</span></span>
    <span class="paper-date">1 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2605.31444">Answer-Set-Programming-based Abstractions for Reinforcement Learning</a>
  <p class="weekly-paper-contribution">This paper introduces an Answer-Set Programming (ASP)-based implementation of the CARCASS framework for relational reinforcement learning, enabling efficient abstractions in complex domains using domain knowledge.</p>
</div>

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#5</span>
    <span class="rel-dots" aria-label="Relevance: 3 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot"></span><span class="rel-dot"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span></span>
    <span class="paper-date">1 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2605.30664">Structure-Induced Information for Rerooting Levin Tree Search</a>
  <p class="weekly-paper-contribution">This paper introduces three rerooter designs for scalable subgoal-free policy tree search, enabling efficient search in complex environments without explicit subgoal generation.</p>
</div>

</div>

<h4>Robotics</h4>
<div class="weekly-paper-list">

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#1</span>
    <span class="rel-dots" aria-label="Relevance: 4 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span></span>
    <span class="paper-date">1 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2605.30542">Physically Viable World Models: A Case for Query-Conditioned Embodied AI</a>
  <p class="weekly-paper-contribution">This paper introduces a framework for physically viable world models in embodied AI that prioritize answering intervention queries through structural physical abstractions, rather than mere observation prediction.</p>
</div>

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#2</span>
    <span class="rel-dots" aria-label="Relevance: 4 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span><span class="cat-tag cat-ml" title="Machine Learning (cs.LG)">Machine Learning (cs.LG)</span><span class="cat-tag cat-ai" title="Multiagent Systems (cs.MA)">Multiagent Systems (cs.MA)</span></span>
    <span class="paper-date">1 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2605.31023">HADT: A Heterogeneous Multi-Agent Differential Transformer for Autonomous Earth Observation Satellite Cluster</a>
  <p class="weekly-paper-contribution">This work introduces HADT, a novel transformer-based architecture for autonomous resource management in heterogeneous satellite clusters conducting Earth Observation missions, demonstrating significant performance improvements over existing baselines.</p>
</div>

</div>

<h2 id="news">Top News</h2>

<div class="news-item">
  <div class="news-meta">
    <span class="news-source news-source--hn">Hacker News</span>
    <span class="news-date">Sun, 31 Ma</span>
  </div>
  <a class="news-title" href="https://www.promptarmor.com/resources/gpt-for-google-sheets-data-exfiltration" target="_blank" rel="noopener noreferrer">ChatGPT for Google Sheets exfiltrates workbooks</a>
  <p class="news-summary">The article highlights a security vulnerability where integrating ChatGPT with Google Sheets can lead to unauthorized data exfiltration, raising concerns about AI-driven data leakage risks.</p>
  <div class="news-footer">
    <div class="news-tags"><span class="news-tag">LLM</span><span class="news-tag">AI Safety</span><span class="news-tag">Data Security</span></div>
    <a class="news-read-btn" href="https://www.promptarmor.com/resources/gpt-for-google-sheets-data-exfiltration" target="_blank" rel="noopener noreferrer">Read&nbsp;more&nbsp;&#8594;</a>
  </div>
</div>

<div class="news-item">
  <div class="news-meta">
    <span class="news-source news-source--hn">Hacker News</span>
    <span class="news-date">Sun, 31 Ma</span>
  </div>
  <a class="news-title" href="https://darylcecile.net/notes/speed-of-prototyping-age-of-ai" target="_blank" rel="noopener noreferrer">The Speed of Prototyping in the Age of AI</a>
  <p class="news-summary">The article discusses how advancements in AI have significantly accelerated the prototyping process, enabling faster development and iteration of AI models. It explores tools and methodologies that reduce the time required to move from concept to implementation in AI projects.</p>
  <div class="news-footer">
    <div class="news-tags"><span class="news-tag">MLOps</span><span class="news-tag">Computing Systems</span><span class="news-tag">AI</span></div>
    <a class="news-read-btn" href="https://darylcecile.net/notes/speed-of-prototyping-age-of-ai" target="_blank" rel="noopener noreferrer">Read&nbsp;more&nbsp;&#8594;</a>
  </div>
</div>

<div class="news-item">
  <div class="news-meta">
    <span class="news-source news-source--nvidia">NVIDIA Technical Blog</span>
    <span class="news-date">2026-06-01</span>
  </div>
  <a class="news-title" href="https://developer.nvidia.com/blog/advancing-ai-infrastructure-for-agentic-ai-with-nvidia-doca-in-silicon-security/" target="_blank" rel="noopener noreferrer">Advancing AI Infrastructure for Agentic AI with NVIDIA DOCA In-Silicon Security</a>
  <p class="news-summary">NVIDIA discusses advancements in AI infrastructure to support agentic AI systems, emphasizing secure, high-performance computing frameworks enabled by DOCA In-Silicon Security. The focus is on building &#x27;AI factories&#x27; that empower autonomous agents with unprecedented capabilities.</p>
  <div class="news-footer">
    <div class="news-tags"><span class="news-tag">Agentic AI</span><span class="news-tag">Computing Systems</span><span class="news-tag">AI Safety</span></div>
    <a class="news-read-btn" href="https://developer.nvidia.com/blog/advancing-ai-infrastructure-for-agentic-ai-with-nvidia-doca-in-silicon-security/" target="_blank" rel="noopener noreferrer">Read&nbsp;more&nbsp;&#8594;</a>
  </div>
</div>

<div class="news-item">
  <div class="news-meta">
    <span class="news-source news-source--nvidia">NVIDIA Technical Blog</span>
    <span class="news-date">2026-06-01</span>
  </div>
  <a class="news-title" href="https://developer.nvidia.com/blog/nvidia-vera-cpu-sets-a-new-standard-for-agentic-workloads-in-ai-factories/" target="_blank" rel="noopener noreferrer">NVIDIA Vera CPU Sets a New Standard for Agentic Workloads in AI Factories</a>
  <p class="news-summary">NVIDIA introduces the Vera CPU, designed to optimize agentic workloads in AI factories by addressing scaling challenges through advanced computing architecture. The development aligns with evolving AI scaling laws, emphasizing efficiency for complex tasks like autonomous systems and large-scale AI operations.</p>
  <div class="news-footer">
    <div class="news-tags"><span class="news-tag">Agentic AI</span><span class="news-tag">Computing Systems</span><span class="news-tag">MLOps</span></div>
    <a class="news-read-btn" href="https://developer.nvidia.com/blog/nvidia-vera-cpu-sets-a-new-standard-for-agentic-workloads-in-ai-factories/" target="_blank" rel="noopener noreferrer">Read&nbsp;more&nbsp;&#8594;</a>
  </div>
</div>

<div class="news-item">
  <div class="news-meta">
    <span class="news-source news-source--nvidia">NVIDIA Technical Blog</span>
    <span class="news-date">2026-05-29</span>
  </div>
  <a class="news-title" href="https://developer.nvidia.com/blog/dynosim-simulating-the-pareto-frontier/" target="_blank" rel="noopener noreferrer">DynoSim: Simulating the Pareto Frontier</a>
  <p class="news-summary">NVIDIA introduces DynoSim, a tool for optimizing large language model (LLM) deployments by simulating trade-offs in system configurations like tensor-parallel shapes and worker splits, enabling efficient tuning of complex deployment stacks.</p>
  <div class="news-footer">
    <div class="news-tags"><span class="news-tag">LLM</span><span class="news-tag">MLOps</span><span class="news-tag">Optimization</span></div>
    <a class="news-read-btn" href="https://developer.nvidia.com/blog/dynosim-simulating-the-pareto-frontier/" target="_blank" rel="noopener noreferrer">Read&nbsp;more&nbsp;&#8594;</a>
  </div>
</div>

<div class="news-item">
  <div class="news-meta">
    <span class="news-source news-source--nvidia">NVIDIA Technical Blog</span>
    <span class="news-date">2026-06-01</span>
  </div>
  <a class="news-title" href="https://developer.nvidia.com/blog/nvidia-dsx-os-delivers-open-modular-software-for-operating-ai-factories-at-scale/" target="_blank" rel="noopener noreferrer">NVIDIA DSX OS Delivers Open, Modular Software for Operating AI Factories at Scale</a>
  <p class="news-summary">NVIDIA introduces DSX OS, an open and modular software platform designed to scale AI factories that generate intelligence through token-based workflows, addressing growing demands for AI infrastructure.</p>
  <div class="news-footer">
    <div class="news-tags"><span class="news-tag">MLOps</span><span class="news-tag">AI Infrastructure</span><span class="news-tag">Scaling</span><span class="news-tag">NVIDIA DSX OS</span></div>
    <a class="news-read-btn" href="https://developer.nvidia.com/blog/nvidia-dsx-os-delivers-open-modular-software-for-operating-ai-factories-at-scale/" target="_blank" rel="noopener noreferrer">Read&nbsp;more&nbsp;&#8594;</a>
  </div>
</div>

<div class="news-item">
  <div class="news-meta">
    <span class="news-source news-source--reddit">Reddit r/MachineLearning</span>
    <span class="news-date">2026-05-31</span>
  </div>
  <a class="news-title" href="https://www.reddit.com/r/MachineLearning/comments/1tsipvv/d_monthly_whos_hiring_and_who_wants_to_be_hired/" target="_blank" rel="noopener noreferrer">[D] Monthly Who&#x27;s Hiring and Who wants to be Hired?</a>
  <p class="news-summary">A monthly Reddit thread for Machine Learning professionals to post job openings or seek employment, using standardized templates for location, salary, work arrangement, and role descriptions. The community emphasizes experience-level alignment.</p>
  <div class="news-footer">
    <div class="news-tags"><span class="news-tag">Job Market</span><span class="news-tag">Careers</span><span class="news-tag">Community</span><span class="news-tag">Hiring</span><span class="news-tag">ML Community</span></div>
    <a class="news-read-btn" href="https://www.reddit.com/r/MachineLearning/comments/1tsipvv/d_monthly_whos_hiring_and_who_wants_to_be_hired/" target="_blank" rel="noopener noreferrer">Read&nbsp;more&nbsp;&#8594;</a>
  </div>
</div>

<div class="news-item">
  <div class="news-meta">
    <span class="news-source news-source--reddit">Reddit r/MachineLearning</span>
    <span class="news-date">2026-06-01</span>
  </div>
  <a class="news-title" href="https://www.reddit.com/r/MachineLearning/comments/1ttei2r/whats_the_actual_focus_in_world_models_right_now_r/" target="_blank" rel="noopener noreferrer">What’s the actual focus in World Models right now? [R]</a>
  <p class="news-summary">The post questions the shift from self-supervised learning methods like Barlow Twins and DINO to scaled-up video generation in industry, while seeking to understand the current academic research focus on World Models.</p>
  <div class="news-footer">
    <div class="news-tags"><span class="news-tag">Computer Vision</span><span class="news-tag">AI Safety</span><span class="news-tag">General</span><span class="news-tag">Agentic AI</span><span class="news-tag">World Models</span></div>
    <a class="news-read-btn" href="https://www.reddit.com/r/MachineLearning/comments/1ttei2r/whats_the_actual_focus_in_world_models_right_now_r/" target="_blank" rel="noopener noreferrer">Read&nbsp;more&nbsp;&#8594;</a>
  </div>
</div>

<div class="news-item">
  <div class="news-meta">
    <span class="news-source news-source--reddit">Reddit r/MachineLearning</span>
    <span class="news-date">2026-05-31</span>
  </div>
  <a class="news-title" href="https://www.reddit.com/r/MachineLearning/comments/1tt7jt2/arabic_asr_model_struggling_to_converge_during/" target="_blank" rel="noopener noreferrer">Arabic ASR model struggling to converge during training [D]</a>
  <p class="news-summary">A user is struggling to train a dialectal Arabic ASR model using SpeechBrain&#x27;s LibriSpeech recipe, facing plateauing CTC and KL divergence losses despite various hyperparameter adjustments. The model fails to converge, resulting in near-100% validation WER, with the dataset being weakly labeled and non-public.</p>
  <div class="news-footer">
    <div class="news-tags"><span class="news-tag">Speech</span><span class="news-tag">NLP</span><span class="news-tag">MLOps</span></div>
    <a class="news-read-btn" href="https://www.reddit.com/r/MachineLearning/comments/1tt7jt2/arabic_asr_model_struggling_to_converge_during/" target="_blank" rel="noopener noreferrer">Read&nbsp;more&nbsp;&#8594;</a>
  </div>
</div>

<div class="news-item">
  <div class="news-meta">
    <span class="news-source news-source--reddit">Reddit r/MachineLearning</span>
    <span class="news-date">2026-05-30</span>
  </div>
  <a class="news-title" href="https://www.reddit.com/r/MachineLearning/comments/1trvuxb/why_do_the_output_layer_weights_become_word/" target="_blank" rel="noopener noreferrer">Why do the output layer weights become word vectors in Word2Vec? [D]</a>
  <p class="news-summary">A user seeks an intuitive and mathematical explanation for why the output layer weights in Word2Vec models encode semantic word representations, questioning why these parameters capture meaningful linguistic features rather than just serving predictive roles.</p>
  <div class="news-footer">
    <div class="news-tags"><span class="news-tag">NLP</span><span class="news-tag">Word2Vec</span><span class="news-tag">Neural Networks</span><span class="news-tag">Embeddings</span><span class="news-tag">Machine Learning</span></div>
    <a class="news-read-btn" href="https://www.reddit.com/r/MachineLearning/comments/1trvuxb/why_do_the_output_layer_weights_become_word/" target="_blank" rel="noopener noreferrer">Read&nbsp;more&nbsp;&#8594;</a>
  </div>
</div>


<h2 id="repos">Trending Repos</h2>
<p class="section-desc">Top repositories this week, sorted by stars.</p>

<div class="weekly-repo-list">

<div class="weekly-repo-item">
  <div class="weekly-repo-header">
    <span class="weekly-rank">#1</span>
    <a class="gh-repo-link" href="https://github.com/FareedKhan-dev/train-llm-from-scratch" target="_blank" rel="noopener noreferrer">
      <span class="gh-owner">FareedKhan-dev</span><span class="gh-sep">/</span><strong class="gh-repo">train-llm-from-scratch</strong>
    </a>
    <span class="gh-topic-pill">LLM</span>
    <span class="weekly-stars">&#9733; 0</span>
  </div>
  <p class="gh-summary">This repository provides a comprehensive guide to training large language models from scratch, covering data preparation to text generation. It is highly relevant as it addresses core LLM development techniques essential for research in agentic AI, foundation models, and MLOps.</p>
  <div class="gh-tags"><span class="gh-tag">llm</span><span class="gh-tag">transformer</span><span class="gh-tag">deep learning</span><span class="gh-tag">fine-tuning</span></div>
</div>

<div class="weekly-repo-item">
  <div class="weekly-repo-header">
    <span class="weekly-rank">#2</span>
    <a class="gh-repo-link" href="https://github.com/jamwithai/production-agentic-rag-course" target="_blank" rel="noopener noreferrer">
      <span class="gh-owner">jamwithai</span><span class="gh-sep">/</span><strong class="gh-repo">production-agentic-rag-course</strong>
    </a>
    <span class="gh-topic-pill">Agentic AI</span>
    <span class="weekly-stars">&#9733; 0</span>
  </div>
  <p class="gh-summary">This repository is a course focused on building production-grade agentic systems using Retrieval-Augmented Generation (RAG), directly addressing the user&#x27;s interests in Agentic AI, RAG, and LLM applications. It likely provides practical implementations of autonomous agents leveraging retrieval and generation techniques for real-world tasks.</p>
  <div class="gh-tags"><span class="gh-tag">agentic-ai</span><span class="gh-tag">rag</span><span class="gh-tag">llm</span></div>
</div>

<div class="weekly-repo-item">
  <div class="weekly-repo-header">
    <span class="weekly-rank">#3</span>
    <a class="gh-repo-link" href="https://github.com/anthropics/claude-code" target="_blank" rel="noopener noreferrer">
      <span class="gh-owner">anthropics</span><span class="gh-sep">/</span><strong class="gh-repo">claude-code</strong>
    </a>
    <span class="gh-topic-pill">Agentic AI</span>
    <span class="weekly-stars">&#9733; 0</span>
  </div>
  <p class="gh-summary">Claude Code is an agentic coding tool that integrates natural language processing with codebase interaction, enabling tasks like code explanation, git workflow management, and task automation. It directly advances research in Agentic AI by demonstrating practical applications of autonomous agents in software development workflows.</p>
  <div class="gh-tags"><span class="gh-tag">Agentic AI</span><span class="gh-tag">LLM</span><span class="gh-tag">NLP</span><span class="gh-tag">agents</span></div>
</div>

<div class="weekly-repo-item">
  <div class="weekly-repo-header">
    <span class="weekly-rank">#4</span>
    <a class="gh-repo-link" href="https://github.com/langchain-ai/rag-from-scratch" target="_blank" rel="noopener noreferrer">
      <span class="gh-owner">langchain-ai</span><span class="gh-sep">/</span><strong class="gh-repo">rag-from-scratch</strong>
    </a>
    <span class="gh-topic-pill">LLM</span>
    <span class="weekly-stars">&#9733; 0</span>
  </div>
  <p class="gh-summary">This repository provides a hands-on implementation of Retrieval-Augmented Generation (RAG) systems, a critical technique for enhancing LLMs with external knowledge. It directly addresses the user&#x27;s interest in &#x27;rag&#x27; and &#x27;llm&#x27;, offering foundational insights into combining retrieval and generation for improved AI performance.</p>
  <div class="gh-tags"><span class="gh-tag">llm</span><span class="gh-tag">rag</span><span class="gh-tag">retrieval</span><span class="gh-tag">vector</span></div>
</div>

<div class="weekly-repo-item">
  <div class="weekly-repo-header">
    <span class="weekly-rank">#5</span>
    <a class="gh-repo-link" href="https://github.com/OpenBMB/VoxCPM" target="_blank" rel="noopener noreferrer">
      <span class="gh-owner">OpenBMB</span><span class="gh-sep">/</span><strong class="gh-repo">VoxCPM</strong>
    </a>
    <span class="gh-topic-pill">Speech</span>
    <span class="weekly-stars">&#9733; 0</span>
  </div>
  <p class="gh-summary">VoxCPM2 is a tokenizer-free TTS model enabling multilingual speech generation, voice cloning, and creative audio design. It advances speech synthesis and generative models, aligning with interests in speech technology and AI-driven audio creation.</p>
  <div class="gh-tags"><span class="gh-tag">speech</span><span class="gh-tag">generative models</span><span class="gh-tag">TTS</span><span class="gh-tag">multilingual</span></div>
</div>

<div class="weekly-repo-item">
  <div class="weekly-repo-header">
    <span class="weekly-rank">#6</span>
    <a class="gh-repo-link" href="https://github.com/revfactory/harness" target="_blank" rel="noopener noreferrer">
      <span class="gh-owner">revfactory</span><span class="gh-sep">/</span><strong class="gh-repo">harness</strong>
    </a>
    <span class="gh-topic-pill">Agentic AI</span>
    <span class="weekly-stars">&#9733; 0</span>
  </div>
  <p class="gh-summary">This repository focuses on designing domain-specific agent teams and generating specialized agent skills, directly aligning with agentic AI research. Its emphasis on structuring collaborative agents is relevant to multi-agent systems and embodied AI applications.</p>
  <div class="gh-tags"><span class="gh-tag">agentic-ai</span><span class="gh-tag">multi-agent-systems</span><span class="gh-tag">mlops</span><span class="gh-tag">llm</span></div>
</div>

<div class="weekly-repo-item">
  <div class="weekly-repo-header">
    <span class="weekly-rank">#7</span>
    <a class="gh-repo-link" href="https://github.com/harry0703/MoneyPrinterTurbo" target="_blank" rel="noopener noreferrer">
      <span class="gh-owner">harry0703</span><span class="gh-sep">/</span><strong class="gh-repo">MoneyPrinterTurbo</strong>
    </a>
    <span class="gh-topic-pill">LLM</span>
    <span class="weekly-stars">&#9733; 0</span>
  </div>
  <p class="gh-summary">This repository leverages AI large language models to generate high-definition short videos with one click. It is highly relevant to LLMs and generative models, demonstrating practical applications of AI in video creation, which aligns with interests in multimodal learning and generative AI.</p>
  <div class="gh-tags"><span class="gh-tag">LLM</span><span class="gh-tag">generative models</span><span class="gh-tag">computer vision</span></div>
</div>

<div class="weekly-repo-item">
  <div class="weekly-repo-header">
    <span class="weekly-rank">#8</span>
    <a class="gh-repo-link" href="https://github.com/nicobailon/pi-subagents" target="_blank" rel="noopener noreferrer">
      <span class="gh-owner">nicobailon</span><span class="gh-sep">/</span><strong class="gh-repo">pi-subagents</strong>
    </a>
    <span class="gh-topic-pill">Agentic AI</span>
    <span class="weekly-stars">&#9733; 0</span>
  </div>
  <p class="gh-summary">This repository extends the Pi framework to enable asynchronous subagent delegation with features like truncation, artifacts, and session sharing. It directly addresses challenges in agentic AI by enabling coordinated task execution across subagents, which is critical for complex multi-agent systems and embodied AI applications.</p>
  <div class="gh-tags"><span class="gh-tag">agentic-ai</span><span class="gh-tag">multi-agent-systems</span><span class="gh-tag">async-delegation</span><span class="gh-tag">session-sharing</span></div>
</div>

<div class="weekly-repo-item">
  <div class="weekly-repo-header">
    <span class="weekly-rank">#9</span>
    <a class="gh-repo-link" href="https://github.com/Comfy-Org/ComfyUI" target="_blank" rel="noopener noreferrer">
      <span class="gh-owner">Comfy-Org</span><span class="gh-sep">/</span><strong class="gh-repo">ComfyUI</strong>
    </a>
    <span class="gh-topic-pill">Computer Vision</span>
    <span class="weekly-stars">&#9733; 0</span>
  </div>
  <p class="gh-summary">ComfyUI is a modular GUI and backend for diffusion models, enabling advanced image generation and manipulation. It is highly relevant to computer vision research, particularly in generative models and multimodal applications.</p>
  <div class="gh-tags"><span class="gh-tag">diffusion</span><span class="gh-tag">computer vision</span><span class="gh-tag">generative models</span><span class="gh-tag">GUI</span></div>
</div>

<div class="weekly-repo-item">
  <div class="weekly-repo-header">
    <span class="weekly-rank">#10</span>
    <a class="gh-repo-link" href="https://github.com/ai-boost/awesome-harness-engineering" target="_blank" rel="noopener noreferrer">
      <span class="gh-owner">ai-boost</span><span class="gh-sep">/</span><strong class="gh-repo">awesome-harness-engineering</strong>
    </a>
    <span class="gh-topic-pill">Agentic AI</span>
    <span class="weekly-stars">&#9733; 0</span>
  </div>
  <p class="gh-summary">This repository curates tools and patterns for AI agent harness engineering, focusing on orchestration, observability, and permissions—critical for building and managing multi-agent systems. It directly supports research and development in agentic AI by addressing infrastructure and operational challenges.</p>
  <div class="gh-tags"><span class="gh-tag">agentic-ai</span><span class="gh-tag">mlops</span><span class="gh-tag">ai-agents</span><span class="gh-tag">observability</span></div>
</div>

</div>
