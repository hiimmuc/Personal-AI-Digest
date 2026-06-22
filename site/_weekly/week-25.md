---
layout: modern
title: "Week 25 — 2026-06-15 – 2026-06-21"
week: 25
paper_count: 86
news_count: 48
repo_count: 15
permalink: /weekly/25/
---

<div class="weekly-stats-bar">
  <span class="weekly-stat"><strong>86</strong> papers</span>
  <span class="weekly-stat-sep">·</span>
  <span class="weekly-stat"><strong>48</strong> news</span>
  <span class="weekly-stat-sep">·</span>
  <span class="weekly-stat"><strong>15</strong> repos</span>
  <span class="weekly-stat-sep">·</span>
  <span class="weekly-stat">Week <strong>25</strong></span>
</div>

<div class="weekly-narrative">
  <p>This week’s developments signal a decisive shift toward the maturation of autonomous agentic workflows, moving beyond simple prompting toward complex orchestration, skill auditing, and proactive communication policies. A significant portion of the research focuses on the &quot;agentic infrastructure&quot; layer, specifically addressing critical bottlenecks such as trust calibration, privacy-aware sanitization, and the &quot;verifier tax&quot; inherent in tool-using models. Simultaneously, the geopolitical and regulatory landscape is hardening, evidenced by the US classifying frontier AI as a controlled export similar to high-end hardware. Community activity reflects a dual interest in high-level abstraction—seen in the popularity of open-source agent frameworks like OpenHands—and the practical democratization of local deployment and data indexing. Collectively, these trends suggest that the industry is transitioning from exploring what models can say to engineering how agents can safely and reliably act.</p>
</div>

<hr>

<h2 id="papers">Research Highlights</h2>

<h3 id="papers-by-interest">By Personal Interest</h3>
<p class="section-desc">Top papers per interest topic, ranked by relevance.</p>

<h4>Multi-Agent Systems</h4>
<div class="weekly-paper-list">

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#1</span>
    <span class="rel-dots" aria-label="Relevance: 3 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot"></span><span class="rel-dot"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-security" title="Cryptography and Security (cs.CR)">Cryptography and Security (cs.CR)</span><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span></span>
    <span class="paper-date">12 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2606.14517">From Shield to Target: Denial-of-Service Attacks on LLM-Based Agent Guardrails</a>
  <p class="weekly-paper-contribution">The paper identifies a novel Denial-of-Service (DoS) vulnerability in LLM-based guardrails where attackers can trigger extended reasoning loops to paralyze autonomous agents. It provides systematic attack frameworks and demonstrates that a single poisoned document can saturate shared guardrail infrastructures.</p>
</div>

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#2</span>
    <span class="rel-dots" aria-label="Relevance: 3 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot"></span><span class="rel-dot"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ai" title="Multiagent Systems (cs.MA)">Multiagent Systems (cs.MA)</span><span class="cat-tag cat-nlp" title="Computation and Language (cs.CL)">Computation and Language (cs.CL)</span></span>
    <span class="paper-date">15 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2606.16710">Misinformation Propagation in Benign Multi-Agent Systems</a>
  <p class="weekly-paper-contribution">The paper investigates how intent-based misinformation propagates within multi-agent systems and identifies how group composition and decision protocols influence robustness.</p>
</div>

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#3</span>
    <span class="rel-dots" aria-label="Relevance: 3 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot"></span><span class="rel-dot"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-eess" title="eess.SY">eess.SY</span><span class="cat-tag cat-ai" title="Multiagent Systems (cs.MA)">Multiagent Systems (cs.MA)</span><span class="cat-tag cat-ro" title="Robotics (cs.RO)">Robotics (cs.RO)</span><span class="cat-tag cat-math" title="math.DS">math.DS</span></span>
    <span class="paper-date">15 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2606.16116">Distributed Safe Consensus Under Asymmetric Input and Time-Varying Output Constraints</a>
  <p class="weekly-paper-contribution">The paper proposes a distributed consensus framework for multi-agent systems that simultaneously handles asymmetric actuator constraints and time-varying output safety constraints.</p>
</div>

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#4</span>
    <span class="rel-dots" aria-label="Relevance: 3 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot"></span><span class="rel-dot"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ai" title="Multiagent Systems (cs.MA)">Multiagent Systems (cs.MA)</span><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span></span>
    <span class="paper-date">14 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2606.15931">DeepRoot: A KG-Coordinated Multi-Agent System for Therapeutic Reasoning over Historical Medical Texts</a>
  <p class="weekly-paper-contribution">The paper introduces DeepRoot, a multi-agent LLM system that successfully converts non-standardized historical medical prose into verifiable drug-discovery leads by separating grounding from reasoning.</p>
</div>

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#5</span>
    <span class="rel-dots" aria-label="Relevance: 3 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot"></span><span class="rel-dot"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-dc" title="Distributed, Parallel, and Cluster Computing (cs.DC)">Distributed, Parallel, and Cluster Computing (cs.DC)</span><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span><span class="cat-tag cat-ai" title="Multiagent Systems (cs.MA)">Multiagent Systems (cs.MA)</span></span>
    <span class="paper-date">13 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2606.15376">CoAgent: Concurrency Control for Multi-Agent Systems</a>
  <p class="weekly-paper-contribution">The paper introduces CoAgent, a concurrency control framework designed specifically for multi-agent LLM systems where classical locking and optimistic concurrency control (OCC) fail due to long inference times and opaque read sets.</p>
</div>

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#6</span>
    <span class="rel-dots" aria-label="Relevance: 3 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot"></span><span class="rel-dot"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-eess" title="eess.SY">eess.SY</span></span>
    <span class="paper-date">13 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2606.15135">Differentially Private Consensus for Time-Delay Multi-agent Systems</a>
  <p class="weekly-paper-contribution">The paper establishes a framework for achieving differentially private consensus in discrete-time multi-agent systems subject to communication delays while protecting the entire delayed initial histories of all agents.</p>
</div>

</div>

<h3 id="papers-by-area">By Research Area</h3>
<p class="section-desc">Top papers per ArXiv subject category, ranked by relevance.</p>

<h4>AI Safety</h4>
<div class="weekly-paper-list">

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#1</span>
    <span class="rel-dots" aria-label="Relevance: 5 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span><span class="cat-tag cat-nlp" title="Computation and Language (cs.CL)">Computation and Language (cs.CL)</span><span class="cat-tag cat-ai" title="Multiagent Systems (cs.MA)">Multiagent Systems (cs.MA)</span></span>
    <span class="paper-date">15 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2606.13715">WorkBench Revisited: Workplace Agents Two Years On</a>
  <p class="weekly-paper-contribution">The paper provides a longitudinal evaluation of agentic performance on the WorkBench benchmark, demonstrating significant improvements in both task completion and safety over a two-year period.</p>
</div>

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#2</span>
    <span class="rel-dots" aria-label="Relevance: 5 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span></span>
    <span class="paper-date">15 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2606.13884">Capability Minimization as a Safety Primitive: Risk-Aware Causal Gating for Least-Privilege LLM Agents</a>
  <p class="weekly-paper-contribution">The paper introduces Risk-Aware Causal Gating (RACG), a framework that prioritizes safety by gating model actions based on counterfactual risk rather than raw predictive confidence. It provides a principled mechanism for least-privilege LLM agents by minimizing the capabilities of a model to perform high-risk actions.</p>
</div>

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#3</span>
    <span class="rel-dots" aria-label="Relevance: 5 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ml" title="Machine Learning (cs.LG)">Machine Learning (cs.LG)</span><span class="cat-tag cat-nlp" title="Computation and Language (cs.CL)">Computation and Language (cs.CL)</span></span>
    <span class="paper-date">15 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2606.13873">Natively Unlearnable Large Language Models</a>
  <p class="weekly-paper-contribution">The paper introduces NULLs (Natively Unlearnable LLMs), a model architecture that enables source-specific unlearning without sacrificing the benefits of joint representation learning. It demonstrates that unlearning can be built natively into the training process rather than as a post-hoc correction.</p>
</div>

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#4</span>
    <span class="rel-dots" aria-label="Relevance: 5 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span></span>
    <span class="paper-date">16 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2606.15034">OSGuard: A Benchmark for Safety in Computer-Use Agents</a>
  <p class="weekly-paper-contribution">The paper introduces OSGuard, a dual-granularity benchmark designed to evaluate the safety of computer-use agents by distinguishing between successful task completion and unsafe shortcuts.</p>
</div>

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#5</span>
    <span class="rel-dots" aria-label="Relevance: 4 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span></span>
    <span class="paper-date">15 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2606.13720">Refusal Beyond a Single Direction: A Preliminary Comparison of Diff-in-Means and INLP</a>
  <p class="weekly-paper-contribution">The paper compares Difference-in-Means (DiM) and Iterative Nullspace Projection (INLP) for steering refusal in LLMs, evaluating whether INLP&#x27;s richer parameterization offers more tunable interventions.</p>
</div>

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#6</span>
    <span class="rel-dots" aria-label="Relevance: 4 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span></span>
    <span class="paper-date">16 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2606.14838">A Definition of Good Explanations and the Challenges Explaining LLM Outputs</a>
  <p class="weekly-paper-contribution">The paper proposes a formal definition of a &#x27;good explanation&#x27; that integrates counterfactual reasoning with the interlocutor&#x27;s prior beliefs. It further identifies specific structural challenges in providing such explanations for Large Language Model (LLM) outputs.</p>
</div>

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#7</span>
    <span class="rel-dots" aria-label="Relevance: 4 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span><span class="cat-tag cat-default" title="Computer Science and Game Theory (cs.GT)">Computer Science and Game Theory (cs.GT)</span><span class="cat-tag cat-physics" title="physics.soc-ph">physics.soc-ph</span></span>
    <span class="paper-date">16 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2606.15078">Cognitive Debt: AI as Intellectual Leverage and the Dynamics of Systemic Fragility</a>
  <p class="weekly-paper-contribution">The paper introduces a formal theory of &#x27;cognitive debt&#x27; to model how using AI as a substitute for first-principles reasoning creates systemic fragility. It identifies a &#x27;cognitive Minsky moment&#x27; where deferred costs and short-run productivity gains mask rising systemic risk.</p>
</div>

</div>

<h4>Agentic AI</h4>
<div class="weekly-paper-list">

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#1</span>
    <span class="rel-dots" aria-label="Relevance: 5 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span><span class="cat-tag cat-nlp" title="Computation and Language (cs.CL)">Computation and Language (cs.CL)</span><span class="cat-tag cat-cv" title="Computer Vision and Pattern Recognition (cs.CV)">Computer Vision and Pattern Recognition (cs.CV)</span></span>
    <span class="paper-date">15 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2606.13707">Orchestra-o1: Omnimodal Agent Orchestration</a>
  <p class="weekly-paper-contribution">The paper introduces Orchestra-o1, a scalable omnimodal agent orchestration framework that enables efficient collaboration across heterogeneous modalities like text, image, audio, and video. It also proposes DA-GRPO, a decision-aligned reinforcement learning approach for training omnimodal agents.</p>
</div>

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#2</span>
    <span class="rel-dots" aria-label="Relevance: 5 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span><span class="cat-tag cat-ml" title="Machine Learning (cs.LG)">Machine Learning (cs.LG)</span></span>
    <span class="paper-date">15 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2606.13710">Hybrid Open-Ended Tri-Evolution Makes Better Deep Researcher</a>
  <p class="weekly-paper-contribution">The paper introduces the Hybrid Open-Ended Tri-Evolution (HOTE) framework, which enables AI agents to autonomously evolve their capabilities for open-ended research tasks by bridging deep research and agent evolution.</p>
</div>

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#3</span>
    <span class="rel-dots" aria-label="Relevance: 5 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span></span>
    <span class="paper-date">15 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2606.13949">Minim: Privacy-Aware Minimal View for Agents via Trusted Local Sanitization</a>
  <p class="weekly-paper-contribution">The paper introduces MINIM, a trusted local broker that performs privacy-aware minimization of UI states to prevent sensitive data leakage when using LLM-powered autonomous agents.</p>
</div>

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#4</span>
    <span class="rel-dots" aria-label="Relevance: 5 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span><span class="cat-tag cat-ml" title="Machine Learning (cs.LG)">Machine Learning (cs.LG)</span></span>
    <span class="paper-date">15 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2606.14200">When Should Agent Trust Be Conditional? Characterizing and Attacking Skill-Conditional Reputation in Agent Swarms</a>
  <p class="weekly-paper-contribution">The paper introduces skill-conditional trust (R(i | k)) as a superior alternative to global reputation scores for heterogeneous agent swarms and identifies a security vulnerability where cross-skill evidence borrowing can be exploited by attackers.</p>
</div>

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#5</span>
    <span class="rel-dots" aria-label="Relevance: 5 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span><span class="cat-tag cat-ml" title="Machine Learning (cs.LG)">Machine Learning (cs.LG)</span></span>
    <span class="paper-date">15 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2606.14211">Closing the Reflection Gap: A Free Calibration Bonus for Agentic RL</a>
  <p class="weekly-paper-contribution">The paper introduces RefGRPO, a method to close the &#x27;reflection gap&#x27; where LLM agents mis-assess their own performance despite receiving concrete environment feedback.</p>
</div>

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#6</span>
    <span class="rel-dots" aria-label="Relevance: 5 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span></span>
    <span class="paper-date">15 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2606.14239">SkillAudit: Ground-Truth-Free Skill Evolution via Paired Trajectory Auditing</a>
  <p class="weekly-paper-contribution">The paper introduces SkillAudit, a framework for evolving agent skills without requiring ground-truth feedback, hidden test outcomes, or environment rewards.</p>
</div>

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#7</span>
    <span class="rel-dots" aria-label="Relevance: 5 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span></span>
    <span class="paper-date">15 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2606.14249">HarnessX: A Composable, Adaptive, and Evolvable Agent Harness Foundry</a>
  <p class="weekly-paper-contribution">The paper introduces HarnessX, a foundry for creating composable, adaptive, and evolvable agent harnesses that move beyond static, hand-crafted scaffolding.</p>
</div>

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#8</span>
    <span class="rel-dots" aria-label="Relevance: 5 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span></span>
    <span class="paper-date">15 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2606.14314">Communication Policy Evolution for Proactive LLM Agents</a>
  <p class="weekly-paper-contribution">The paper formalizes &#x27;Communication Policy&#x27; for proactive LLM agents and introduces a self-evolution framework (CPE) to optimize how agents exchange information across different modalities.</p>
</div>

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#9</span>
    <span class="rel-dots" aria-label="Relevance: 5 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span><span class="cat-tag cat-nlp" title="Computation and Language (cs.CL)">Computation and Language (cs.CL)</span><span class="cat-tag cat-ml" title="Machine Learning (cs.LG)">Machine Learning (cs.LG)</span></span>
    <span class="paper-date">15 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2606.14470">GitOfThoughts: Version-Controlled Reasoning and Agent Memory You Can Replay, Diff, and Merge</a>
  <p class="weekly-paper-contribution">The paper introduces GitOfThoughts, a framework that treats LLM reasoning as a version-controlled repository, and provides a rigorous empirical analysis of memory substrates for LLM accuracy.</p>
</div>

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#10</span>
    <span class="rel-dots" aria-label="Relevance: 5 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span></span>
    <span class="paper-date">15 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2606.14502">From Chatbot to Digital Colleague: The Paradigm Shift Toward Persistent Autonomous AI</a>
  <p class="weekly-paper-contribution">The paper conceptualizes the paradigm shift of LLMs from conversational chatbots to &#x27;Digital Colleagues&#x27; by defining a transition toward persistent autonomous systems capable of reasoning, memory, and self-improvement.</p>
</div>

</div>

<h4>Computer Vision</h4>
<div class="weekly-paper-list">

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#1</span>
    <span class="rel-dots" aria-label="Relevance: 4 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span></span>
    <span class="paper-date">15 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2606.14240">AFFORDANCE20Q: Evaluating Affordance Reasoning from Physical Properties</a>
  <p class="weekly-paper-contribution">The paper introduces Affordance20Q, a new benchmark for evaluating affordance reasoning without object identity exposure, and proposes KARI to improve model performance.</p>
</div>

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#2</span>
    <span class="rel-dots" aria-label="Relevance: 4 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span></span>
    <span class="paper-date">15 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2606.14507">Dense Coordinate-List Fine-Tuning Induces a Controllable Interference Surface in Vision-Language Models</a>
  <p class="weekly-paper-contribution">The paper identifies and characterizes a &#x27;controllable interference surface&#x27; where fine-tuning vision-language models for dense coordinate lists improves grounding but induces structured output artifacts like repetition.</p>
</div>

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#3</span>
    <span class="rel-dots" aria-label="Relevance: 4 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span></span>
    <span class="paper-date">16 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2606.15038">Fusion is not one-size-fits-all: Cross-Modal Representation Alignment for Time-to-Event Modeling</a>
  <p class="weekly-paper-contribution">The paper introduces a foundation model-driven framework for cross-modal representation alignment between CT imaging and longitudinal EHR data for time-to-event (TTE) modeling. It provides the first systematic analysis of how different fusion strategies behave under modality imbalance across diverse clinical tasks.</p>
</div>

</div>

<h4>Computing Systems</h4>
<div class="weekly-paper-list">

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#1</span>
    <span class="rel-dots" aria-label="Relevance: 4 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ml" title="Machine Learning (cs.LG)">Machine Learning (cs.LG)</span></span>
    <span class="paper-date">15 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2606.13740">Efficient On-Device Diffusion LLM Inference with Mobile NPU</a>
  <p class="weekly-paper-contribution">The paper introduces llada.cpp, the first NPU-aware inference framework designed to accelerate diffusion large language models (dLLMs) on mobile devices.</p>
</div>

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#2</span>
    <span class="rel-dots" aria-label="Relevance: 4 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span></span>
    <span class="paper-date">16 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2606.15179">CONCORD: Asynchronous Sparse Aggregation for Device-Cloud RAG under Document Isolation</a>
  <p class="weekly-paper-contribution">The paper introduces CONCORD, an asynchronous sparse aggregation framework designed for device-cloud collaborative RAG where private documents are isolated on the device and public knowledge is in the cloud.</p>
</div>

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#3</span>
    <span class="rel-dots" aria-label="Relevance: 3 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot"></span><span class="rel-dot"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span><span class="cat-tag cat-default" title="Databases (cs.DB)">Databases (cs.DB)</span></span>
    <span class="paper-date">15 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2606.13871">Hyperdimensional computing for structured querying on tabular data embeddings</a>
  <p class="weekly-paper-contribution">The paper introduces a HyperDimensional Computing (HDC) framework for tabular row embeddings that provides interpretable similarity scores and principled thresholds for structured querying. This enables reliable zero-match detection, a significant limitation in existing nearest-neighbor retrieval methods.</p>
</div>

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#4</span>
    <span class="rel-dots" aria-label="Relevance: 2 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot"></span><span class="rel-dot"></span><span class="rel-dot"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ml" title="Machine Learning (cs.LG)">Machine Learning (cs.LG)</span><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span><span class="cat-tag cat-physics" title="physics.comp-ph">physics.comp-ph</span><span class="cat-tag cat-physics" title="physics.flu-dyn">physics.flu-dyn</span><span class="cat-tag cat-ml" title="Machine Learning (Statistics) (stat.ML)">Machine Learning (Statistics) (stat.ML)</span></span>
    <span class="paper-date">15 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2606.13742">A fully GPU-based workflow for building physics emulators of hypersonic flows</a>
  <p class="weekly-paper-contribution">The paper introduces a fully GPU-based workflow that integrates differentiable high-fidelity solvers with neural emulators to create physics-consistent surrogates for hypersonic flows.</p>
</div>

</div>

<h4>General</h4>
<div class="weekly-paper-list">

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#1</span>
    <span class="rel-dots" aria-label="Relevance: 4 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ml" title="Machine Learning (cs.LG)">Machine Learning (cs.LG)</span><span class="cat-tag cat-bio" title="Neurons and Cognition (q-bio.NC)">Neurons and Cognition (q-bio.NC)</span></span>
    <span class="paper-date">15 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2606.13801">Neural Variability Enhances Artificial Network Robustness</a>
  <p class="weekly-paper-contribution">The paper demonstrates that structured neural variability (correlated noise) in artificial neural networks enhances robustness against both adversarial attacks and naturalistic image modifications. It establishes a biologically plausible strategy for improving network stability using only local activation information.</p>
</div>

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#2</span>
    <span class="rel-dots" aria-label="Relevance: 4 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ml" title="Machine Learning (cs.LG)">Machine Learning (cs.LG)</span></span>
    <span class="paper-date">15 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2606.13818">Uncertainty Estimation and Generalization Bounds for Modern Deep Learning</a>
  <p class="weekly-paper-contribution">The thesis provides a unified probabilistic framework connecting diversity, smoothness, and stochasticity to explain generalization in over-parameterized networks while introducing scalable Bayesian methods for uncertainty estimation.</p>
</div>

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#3</span>
    <span class="rel-dots" aria-label="Relevance: 4 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span><span class="cat-tag cat-ml" title="Machine Learning (cs.LG)">Machine Learning (cs.LG)</span><span class="cat-tag cat-default" title="cs.SI">cs.SI</span><span class="cat-tag cat-ml" title="Machine Learning (Statistics) (stat.ML)">Machine Learning (Statistics) (stat.ML)</span></span>
    <span class="paper-date">16 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2606.14892">Relational Structural Causal Models</a>
  <p class="weekly-paper-contribution">The paper introduces Relational Structural Causal Models (RSCMs), a framework that extends structural causal models to environments with varying numbers and types of objects. It provides symbolic identification criteria for relational queries and a provably correct neural implementation.</p>
</div>

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#4</span>
    <span class="rel-dots" aria-label="Relevance: 4 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span><span class="cat-tag cat-ml" title="Machine Learning (cs.LG)">Machine Learning (cs.LG)</span></span>
    <span class="paper-date">16 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2606.14997">AI Engram: In Search of Memory Traces in Artificial Intelligence</a>
  <p class="weekly-paper-contribution">The paper introduces a geometric framework to identify and isolate &#x27;AI engrams&#x27;—specific memory traces within deep neural networks—bridging biological memory theories with artificial representation learning.</p>
</div>

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#5</span>
    <span class="rel-dots" aria-label="Relevance: 3 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot"></span><span class="rel-dot"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span></span>
    <span class="paper-date">15 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2606.13734">AI Receptivity or AI Adoption Breadth? A Tool-Specific Reanalysis of the Lower-Literacy/Higher-Usage Link</a>
  <p class="weekly-paper-contribution">The paper challenges the claim that lower AI literacy predicts general AI receptivity by demonstrating that this relationship is actually specific to non-text AI tools. It reveals that the perceived link is a result of aggregate data masking significant heterogeneity across different AI categories.</p>
</div>

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#6</span>
    <span class="rel-dots" aria-label="Relevance: 3 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot"></span><span class="rel-dot"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span></span>
    <span class="paper-date">15 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2606.14176">VeriGeo: Controllable Geometry Question Generation with Numerical and Analytical Verification</a>
  <p class="weekly-paper-contribution">The paper introduces VeriGeo, a framework for generating controllable and verifiable geometry problems with consistent diagrams, constraints, and solutions. It also demonstrates that fine-tuning on this verified synthetic data significantly improves multimodal geometry reasoning performance.</p>
</div>

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#7</span>
    <span class="rel-dots" aria-label="Relevance: 3 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot"></span><span class="rel-dot"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ml" title="Machine Learning (cs.LG)">Machine Learning (cs.LG)</span><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span></span>
    <span class="paper-date">15 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2606.13753">The Weight Norm Sets the Grokking Timescale: A Causal Delay Law</a>
  <p class="weekly-paper-contribution">The paper establishes a causal link between weight norm and grokking timescales by demonstrating that the delay follows an exponential law when the norm is clamped.</p>
</div>

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#8</span>
    <span class="rel-dots" aria-label="Relevance: 3 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot"></span><span class="rel-dot"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ml" title="Machine Learning (cs.LG)">Machine Learning (cs.LG)</span></span>
    <span class="paper-date">15 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2606.13754">D2H-AD: A Hybrid Model Utilizing Hyperdimensional Computing for Advanced Anomaly Detection</a>
  <p class="weekly-paper-contribution">The paper introduces D2H-AD, a novel anomaly detection framework that integrates distance-based similarity and density-aware encoding within a Hyperdimensional Computing (HDC) paradigm. It demonstrates superior performance over traditional deep learning and HDC baselines while maintaining a lightweight footprint suitable for edge AI.</p>
</div>

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#9</span>
    <span class="rel-dots" aria-label="Relevance: 3 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot"></span><span class="rel-dot"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ml" title="Machine Learning (cs.LG)">Machine Learning (cs.LG)</span></span>
    <span class="paper-date">15 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2606.13803">Neural Slack Variables for Shape Constraints</a>
  <p class="weekly-paper-contribution">The paper introduces &#x27;neural slack variables,&#x27; a primal-side approach that converts functional inequality constraints (like monotonicity and convexity) into a regression problem to ensure robust feasibility.</p>
</div>

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#10</span>
    <span class="rel-dots" aria-label="Relevance: 3 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot"></span><span class="rel-dot"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ml" title="Machine Learning (cs.LG)">Machine Learning (cs.LG)</span><span class="cat-tag cat-eess" title="Signal Processing (eess.SP)">Signal Processing (eess.SP)</span><span class="cat-tag cat-ml" title="Machine Learning (Statistics) (stat.ML)">Machine Learning (Statistics) (stat.ML)</span></span>
    <span class="paper-date">15 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2606.13823">A Stationarity-and-Coupling Criterion for Training-Free Time-Lagged Spectral Embeddings of Multivariate Time Series</a>
  <p class="weekly-paper-contribution">The paper introduces a falsifiable applicability criterion to predict when a training-free, time-lagged spectral embedding can successfully distinguish classes in multivariate time series. It provides a two-part pre-flight test (stationarity and power-baseline checks) to determine if a dataset&#x27;s class information resides in cross-channel temporal coupling.</p>
</div>

</div>

<h4>Human-Computer Interaction</h4>
<div class="weekly-paper-list">

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#1</span>
    <span class="rel-dots" aria-label="Relevance: 3 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot"></span><span class="rel-dot"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span><span class="cat-tag cat-nlp" title="Computation and Language (cs.CL)">Computation and Language (cs.CL)</span><span class="cat-tag cat-ml" title="Machine Learning (cs.LG)">Machine Learning (cs.LG)</span></span>
    <span class="paper-date">15 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2606.14654">Abstracting Cross-Domain Action Sequences into Interpretable Workflows</a>
  <p class="weekly-paper-contribution">The paper introduces WorkflowView, a framework that leverages Large Language Models (LLMs) to abstract noisy, low-level digital interaction logs into high-level, interpretable workflows across diverse domains.</p>
</div>

</div>

<h4>LLM</h4>
<div class="weekly-paper-list">

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#1</span>
    <span class="rel-dots" aria-label="Relevance: 5 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ml" title="Machine Learning (cs.LG)">Machine Learning (cs.LG)</span><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span><span class="cat-tag cat-nlp" title="Computation and Language (cs.CL)">Computation and Language (cs.CL)</span></span>
    <span class="paper-date">15 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2606.13862">SuperThoughts: Reasoning Tokens in Superposition</a>
  <p class="weekly-paper-contribution">The paper introduces SuperThoughts, a method to accelerate Long Chain-of-Thought (CoT) reasoning by compressing consecutive tokens into latent representations to improve inference throughput.</p>
</div>

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#2</span>
    <span class="rel-dots" aria-label="Relevance: 4 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span><span class="cat-tag cat-nlp" title="Computation and Language (cs.CL)">Computation and Language (cs.CL)</span></span>
    <span class="paper-date">15 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2606.13683">UP-NRPA: User Portrait based Nested Rollout Policy Adaptation for Planning with Large Language Models in Goal-oriented Dialogue Systems</a>
  <p class="weekly-paper-contribution">The paper introduces UP-NRPA, an online framework that enables dialogue systems to dynamically adapt to diverse user characteristics without requiring offline reinforcement learning or pre-trained group-specific models.</p>
</div>

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#3</span>
    <span class="rel-dots" aria-label="Relevance: 4 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span></span>
    <span class="paper-date">15 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2606.13732">When Sample Selection Bias Precipitates Model Collapse</a>
  <p class="weekly-paper-contribution">The paper identifies that data selection in recursive synthetic training can accelerate model collapse when verifiers use biased, local reference distributions. It provides a theoretical proof of power-law diversity decay in siloed selection and proposes a collaborative Wasserstein proxy reference as a mitigation.</p>
</div>

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#4</span>
    <span class="rel-dots" aria-label="Relevance: 4 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span></span>
    <span class="paper-date">15 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2606.13782">MA-ProofBench: A Two-Tiered Evaluation of LLMs for Theorem Proving in Mathematical Analysis</a>
  <p class="weekly-paper-contribution">The paper introduces MA-ProofBench, the first formal theorem-proving benchmark specifically dedicated to Mathematical Analysis, featuring 200 formalized theorems across two difficulty levels.</p>
</div>

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#5</span>
    <span class="rel-dots" aria-label="Relevance: 4 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span><span class="cat-tag cat-nlp" title="Computation and Language (cs.CL)">Computation and Language (cs.CL)</span></span>
    <span class="paper-date">15 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2606.13815">Poker Arena: Multi-Axis Profiling of Strategic Reasoning and Memory in LLMs</a>
  <p class="weekly-paper-contribution">The paper introduces Poker Arena, a multi-axis evaluation framework that decomposes strategic reasoning into nine distinct cognitive dimensions to reveal the underlying capability structures of LLMs beyond simple scalar scores.</p>
</div>

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#6</span>
    <span class="rel-dots" aria-label="Relevance: 4 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span><span class="cat-tag cat-math" title="math.AG">math.AG</span></span>
    <span class="paper-date">15 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2606.13925">Sorries Are Not the Hard Part: An Expert-Review Case Study of a Semi-Autonomous Formalization</a>
  <p class="weekly-paper-contribution">The paper introduces a new evaluation metric for autoformalization that prioritizes &#x27;expert-review&#x27; quality over mere &#x27;sorry-free&#x27; compilation. It demonstrates that while LLMs can close proof gaps, they often fail to produce reusable, well-structured formal libraries.</p>
</div>

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#7</span>
    <span class="rel-dots" aria-label="Relevance: 4 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span></span>
    <span class="paper-date">15 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2606.13934">Adversarial Concept Search: Predicting Compositional Errors From Feature Geometry</a>
  <p class="weekly-paper-contribution">The paper introduces a method to predict LLM compositional failures by analyzing the geometric relationships between concept representations. It demonstrates that representational interference, rather than just task complexity, is a primary driver of model errors.</p>
</div>

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#8</span>
    <span class="rel-dots" aria-label="Relevance: 4 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span></span>
    <span class="paper-date">15 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2606.14119">FactoryLLM: A Safe and Open-Source AI Playground for Evaluating LLMs in Smart Factories</a>
  <p class="weekly-paper-contribution">The paper introduces FactoryLLM, an open-source, safe AI playground designed to evaluate LLM-based Retrieval-Augmented Generation (RAG) models specifically for cross-machine fault diagnostics in smart factories.</p>
</div>

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#9</span>
    <span class="rel-dots" aria-label="Relevance: 4 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ml" title="Machine Learning (cs.LG)">Machine Learning (cs.LG)</span><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span></span>
    <span class="paper-date">15 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2606.13705">Can Editing 1 Neuron Fix Repetition Loops in LLMs?</a>
  <p class="weekly-paper-contribution">The paper demonstrates that specific repetition loops in LLMs can be localized to a small set of neurons and mitigated through targeted weight surgery. It also establishes a boundary for this method by showing it cannot solve fundamental knowledge-precision issues in long-reasoning tasks.</p>
</div>

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#10</span>
    <span class="rel-dots" aria-label="Relevance: 4 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ml" title="Machine Learning (cs.LG)">Machine Learning (cs.LG)</span><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span><span class="cat-tag cat-default" title="cs.IT">cs.IT</span><span class="cat-tag cat-math" title="math.IT">math.IT</span></span>
    <span class="paper-date">15 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2606.13767">Beyond LoRA: Is Sparsity-Induced Adaptation Better?</a>
  <p class="weekly-paper-contribution">The paper introduces sparsity-induced adaptations for LoRA, specifically Cheap LoRA (cLA) and chained circulant variants (c3LA), and provides the first information-theoretic generalization error bounds for these methods.</p>
</div>

</div>

<h4>MLOps</h4>
<div class="weekly-paper-list">

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#1</span>
    <span class="rel-dots" aria-label="Relevance: 4 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ml" title="Machine Learning (cs.LG)">Machine Learning (cs.LG)</span></span>
    <span class="paper-date">15 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2606.13867">Muon$^p$: Muon with Fractional Spectral Powers</a>
  
</div>

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#2</span>
    <span class="rel-dots" aria-label="Relevance: 4 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ml" title="Machine Learning (cs.LG)">Machine Learning (cs.LG)</span><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span><span class="cat-tag cat-nlp" title="Computation and Language (cs.CL)">Computation and Language (cs.CL)</span><span class="cat-tag cat-cv" title="Computer Vision and Pattern Recognition (cs.CV)">Computer Vision and Pattern Recognition (cs.CV)</span></span>
    <span class="paper-date">15 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2606.13894">Gefen: Optimized Stochastic Optimizer</a>
  <p class="weekly-paper-contribution">The paper introduces Gefen, a memory-efficient optimizer that reduces AdamW&#x27;s memory footprint by approximately 8x while maintaining equivalent performance.</p>
</div>

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#3</span>
    <span class="rel-dots" aria-label="Relevance: 3 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot"></span><span class="rel-dot"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span><span class="cat-tag cat-nlp" title="Computation and Language (cs.CL)">Computation and Language (cs.CL)</span><span class="cat-tag cat-default" title="cs.CY">cs.CY</span></span>
    <span class="paper-date">15 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2606.14516">Every Eval Ever: A Unifying Schema and Community Repository for AI Evaluation Results</a>
  <p class="weekly-paper-contribution">The paper introduces &#x27;Every Eval Ever,&#x27; the first unified metadata schema and community-crowdsourced repository designed to standardize and centralize AI evaluation results.</p>
</div>

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#4</span>
    <span class="rel-dots" aria-label="Relevance: 3 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot"></span><span class="rel-dot"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ml" title="Machine Learning (cs.LG)">Machine Learning (cs.LG)</span></span>
    <span class="paper-date">15 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2606.13748">FedSPC: Shared Parameter Correction for Personalized Federated Learning</a>
  <p class="weekly-paper-contribution">The paper introduces FedSPC, a modular correction method designed to mitigate inconsistent updates to shared parameters in Personalized Federated Learning (PFL) caused by heterogeneous local objectives.</p>
</div>

</div>

<h4>NLP</h4>
<div class="weekly-paper-list">

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#1</span>
    <span class="rel-dots" aria-label="Relevance: 3 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot"></span><span class="rel-dot"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span></span>
    <span class="paper-date">16 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2606.14941">Semantics-Enhanced Retrieval-Augmented Time Series Forecasting</a>
  <p class="weekly-paper-contribution">The paper introduces SERAF, a multimodal framework that enhances time series forecasting by integrating both numerical similarity and semantic descriptions into a retrieval-augmented architecture.</p>
</div>

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#2</span>
    <span class="rel-dots" aria-label="Relevance: 2 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot"></span><span class="rel-dot"></span><span class="rel-dot"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span></span>
    <span class="paper-date">15 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2606.14031">Applicability Condition Extraction for Therapeutic Drug-Disease Relations</a>
  <p class="weekly-paper-contribution">The paper introduces the first dataset for extracting applicability conditions for drug-disease relations and proposes a new method to identify these context-specific conditions from biomedical literature.</p>
</div>

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#3</span>
    <span class="rel-dots" aria-label="Relevance: 2 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot"></span><span class="rel-dot"></span><span class="rel-dot"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ml" title="Machine Learning (cs.LG)">Machine Learning (cs.LG)</span></span>
    <span class="paper-date">15 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2606.13821">Attention-Based Estimation of the Individual Treatment Benefit Probability under Dose Variation</a>
  <p class="weekly-paper-contribution">The paper introduces Dose-AIPTB, a general framework for estimating the Individual Probability of Treatment Benefit (IPTB) for ordinal outcomes under discrete dose variations. It extends IPTB estimation beyond binary treatment settings to accommodate multi-dose clinical scenarios.</p>
</div>

</div>

<h4>RL</h4>
<div class="weekly-paper-list">

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#1</span>
    <span class="rel-dots" aria-label="Relevance: 4 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span><span class="cat-tag cat-ml" title="Machine Learning (cs.LG)">Machine Learning (cs.LG)</span></span>
    <span class="paper-date">15 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2606.13682">A Deep Reinforcement Learning (DRL)-Based Transformer Method for Solving the Open Shop Scheduling Problem</a>
  <p class="weekly-paper-contribution">The paper introduces a Transformer-based Deep Reinforcement Learning policy for the Open Shop Scheduling Problem (OSSP) that generalizes from small-scale benchmarks to large-scale industrial instances.</p>
</div>

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#2</span>
    <span class="rel-dots" aria-label="Relevance: 4 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span></span>
    <span class="paper-date">15 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2606.14415">CSPO: Constraint-Sensitive Policy Optimization for Safe Reinforcement Learning</a>
  <p class="weekly-paper-contribution">The paper introduces CSPO, a first-order primal-dual method for Safe RL that incorporates local constraint sensitivity to mitigate the oscillatory behavior and delayed corrections typical of standard primal-dual methods.</p>
</div>

</div>

<h4>Robotics</h4>
<div class="weekly-paper-list">

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#1</span>
    <span class="rel-dots" aria-label="Relevance: 5 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ai" title="Artificial Intelligence (cs.AI)">Artificial Intelligence (cs.AI)</span><span class="cat-tag cat-ml" title="Machine Learning (cs.LG)">Machine Learning (cs.LG)</span><span class="cat-tag cat-ro" title="Robotics (cs.RO)">Robotics (cs.RO)</span></span>
    <span class="paper-date">15 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2606.14418">Causal Object-Centric Models for Planning with Monte Carlo Tree Search</a>
  <p class="weekly-paper-contribution">The paper introduces COMET, a model-based reinforcement learning algorithm that integrates object-level inductive biases into MuZero-style latent planning. It achieves superior early-stage training performance by performing Monte Carlo Tree Search in a slot-structured latent space.</p>
</div>

<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#2</span>
    <span class="rel-dots" aria-label="Relevance: 5 out of 5"><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span><span class="rel-dot filled"></span></span>
    <span class="cat-tags"><span class="cat-tag cat-ml" title="Machine Learning (cs.LG)">Machine Learning (cs.LG)</span></span>
    <span class="paper-date">15 Jun 2026</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/2606.13795">Diffusion Policy Optimization without Drifting Apart</a>
  <p class="weekly-paper-contribution">The paper introduces DiPOD, a framework that stabilizes diffusion policy optimization by addressing the &#x27;double-drift&#x27; phenomenon where surrogate optimization causes the proxy policy gradient to misalign with the true policy gradient.</p>
</div>

</div>

<h2 id="news">Top News</h2>

<div class="news-item">
  <div class="news-meta">
    <span class="news-source news-source--hn">Hacker News</span>
    <span class="news-date">Mon, 15 Ju</span>
  </div>
  <a class="news-title" href="https://platform.claude.com/docs/en/cli-sdks-libraries/libraries/apple-foundation-models" target="_blank" rel="noopener noreferrer">Apple Foundation Models</a>
  <p class="news-summary">The discussion centers on Apple&#x27;s strategic move toward developing proprietary foundation models to power on-device intelligence. Users are debating the implications for privacy, hardware optimization, and how these models will integrate with the broader Apple ecosystem.</p>
  <div class="news-footer">
    <div class="news-tags"><span class="news-tag">Foundation Models</span><span class="news-tag">On-device AI</span><span class="news-tag">Apple</span><span class="news-tag">LLM</span><span class="news-tag">Privacy</span></div>
    <a class="news-read-btn" href="https://platform.claude.com/docs/en/cli-sdks-libraries/libraries/apple-foundation-models" target="_blank" rel="noopener noreferrer">Read&nbsp;more&nbsp;&#8594;</a>
  </div>
</div>

<div class="news-item">
  <div class="news-meta">
    <span class="news-source news-source--reddit">Reddit r/MachineLearning</span>
    <span class="news-date">2026-06-14</span>
  </div>
  <a class="news-title" href="https://www.reddit.com/r/MachineLearning/comments/1u58mkq/the_verifier_tax_horizondependent_safetysuccess/" target="_blank" rel="noopener noreferrer">The Verifier Tax: Horizon-Dependent Safety–Success Tradeoffs in Tool-Using LLM Agents [R]</a>
  <p class="news-summary">Researchers introduce the &#x27;Verifier Tax,&#x27; a phenomenon where safety verification in tool-using LLM agents leads to a trade-off between safety and task completion as the task horizon increases. The study proposes a two-tier verification architecture—combining deterministic checks with LLM-based verifiers—to mitigate &#x27;unsafe success&#x27; where agents complete goals by violating policies. The findings highlight the complexity of evaluating agentic AI, suggesting that task completion alone is an insufficient metric for safety.</p>
  <div class="news-footer">
    <div class="news-tags"><span class="news-tag">LLM Agents</span><span class="news-tag">AI Safety</span><span class="news-tag">Tool-Use</span><span class="news-tag">Evaluation Metrics</span><span class="news-tag">Verifier Tax</span></div>
    <a class="news-read-btn" href="https://www.reddit.com/r/MachineLearning/comments/1u58mkq/the_verifier_tax_horizondependent_safetysuccess/" target="_blank" rel="noopener noreferrer">Read&nbsp;more&nbsp;&#8594;</a>
  </div>
</div>

<div class="news-item">
  <div class="news-meta">
    <span class="news-source news-source--reddit">Reddit r/ArtificialIntelligence</span>
    <span class="news-date">2026-06-15</span>
  </div>
  <a class="news-title" href="https://www.reddit.com/r/artificial/comments/1u64nok/the_us_just_made_frontier_ai_a_controlled_export/" target="_blank" rel="noopener noreferrer">the US just made frontier ai a controlled export, like nvidia chips</a>
  <p class="news-summary">The US government has placed Anthropic&#x27;s most powerful models, Fable 5 and Mythos 5, under export controls similar to high-end Nvidia chips. This move follows a reported jailbreak of Mythos 5&#x27;s cybersecurity capabilities, leading to a policy where frontier AI is treated as a controlled commodity. The decision establishes a precedent for a two-tier AI world where non-US nationals may be restricted from accessing top-tier frontier models.</p>
  <div class="news-footer">
    <div class="news-tags"><span class="news-tag">AI Governance</span><span class="news-tag">Export Controls</span><span class="news-tag">Anthropic</span><span class="news-tag">Frontier Models</span><span class="news-tag">Cybersecurity</span></div>
    <a class="news-read-btn" href="https://www.reddit.com/r/artificial/comments/1u64nok/the_us_just_made_frontier_ai_a_controlled_export/" target="_blank" rel="noopener noreferrer">Read&nbsp;more&nbsp;&#8594;</a>
  </div>
</div>

<div class="news-item">
  <div class="news-meta">
    <span class="news-source news-source--hn">Hacker News</span>
    <span class="news-date">Tue, 16 Ju</span>
  </div>
  <a class="news-title" href="https://www.economist.com/by-invitation/2026/06/15/humanity-isnt-ready-for-the-coming-intelligence-explosion" target="_blank" rel="noopener noreferrer">Humanity isn&#x27;t ready for the coming intelligence explosion</a>
  <p class="news-summary">The article discusses the existential risks and societal unpreparedness regarding a potential &#x27;intelligence explosion&#x27; driven by rapid AI advancement. It explores the gap between technological capabilities and our current regulatory, ethical, and cognitive frameworks. The piece emphasizes the need for proactive safety measures before AGI reaches a point of no return.</p>
  <div class="news-footer">
    <div class="news-tags"><span class="news-tag">AI Safety</span><span class="news-tag">AGI</span><span class="news-tag">Existential Risk</span><span class="news-tag">Ethics</span><span class="news-tag">Intelligence Explosion</span></div>
    <a class="news-read-btn" href="https://www.economist.com/by-invitation/2026/06/15/humanity-isnt-ready-for-the-coming-intelligence-explosion" target="_blank" rel="noopener noreferrer">Read&nbsp;more&nbsp;&#8594;</a>
  </div>
</div>

<div class="news-item">
  <div class="news-meta">
    <span class="news-source news-source--hn">Hacker News</span>
    <span class="news-date">Sun, 14 Ju</span>
  </div>
  <a class="news-title" href="https://blog.janestreet.com/formal-methods-at-jane-street-index/?from_theconsensus=1" target="_blank" rel="noopener noreferrer">Formal methods and the future of programming</a>
  <p class="news-summary">The article explores the application of formal methods to ensure software correctness and reliability in high-stakes environments. It discusses how mathematical proofs can be used to verify complex systems, moving beyond traditional testing to guarantee behavior. This approach is increasingly relevant as software complexity grows in critical infrastructure and financial systems.</p>
  <div class="news-footer">
    <div class="news-tags"><span class="news-tag">Formal Methods</span><span class="news-tag">Software Engineering</span><span class="news-tag">Systems Programming</span><span class="news-tag">Verification</span><span class="news-tag">Reliability</span></div>
    <a class="news-read-btn" href="https://blog.janestreet.com/formal-methods-at-jane-street-index/?from_theconsensus=1" target="_blank" rel="noopener noreferrer">Read&nbsp;more&nbsp;&#8594;</a>
  </div>
</div>

<div class="news-item">
  <div class="news-meta">
    <span class="news-source news-source--hn">Hacker News</span>
    <span class="news-date">Sun, 14 Ju</span>
  </div>
  <a class="news-title" href="https://news.ycombinator.com/item?id=48528029" target="_blank" rel="noopener noreferrer">I indexed 669 GB of my GoPro videos using my M1 Max computer and local ML models</a>
  <p class="news-summary">A user successfully indexed a massive 669 GB library of GoPro footage using an M1 Max MacBook and local machine learning models. The project demonstrates the feasibility of private, high-volume video content organization using edge computing and local inference.</p>
  <div class="news-footer">
    <div class="news-tags"><span class="news-tag">Computer Vision</span><span class="news-tag">Local ML</span><span class="news-tag">Edge Computing</span><span class="news-tag">Video Indexing</span></div>
    <a class="news-read-btn" href="https://news.ycombinator.com/item?id=48528029" target="_blank" rel="noopener noreferrer">Read&nbsp;more&nbsp;&#8594;</a>
  </div>
</div>

<div class="news-item">
  <div class="news-meta">
    <span class="news-source news-source--reddit">Reddit r/MachineLearning</span>
    <span class="news-date">2026-06-14</span>
  </div>
  <a class="news-title" href="https://www.reddit.com/r/MachineLearning/comments/1u5yyyl/i_built_an_opensource_knowledge_graph_pipeline/" target="_blank" rel="noopener noreferrer">I built an open-source Knowledge Graph pipeline with hybrid retrieval to improve LLM multi-hop reasoning [P]</a>
  <p class="news-summary">A new open-source pipeline combines Knowledge Graphs with hybrid retrieval (Dense Vector + BM25) to enhance LLM multi-hop reasoning. The system uses spaCy for entity extraction, NetworkX for graph construction, and community detection to mitigate &#x27;hub node&#x27; bias. By traversing graph neighbors and using Reciprocal Rank Fusion, it successfully connects disconnected information to answer complex, multi-step queries.</p>
  <div class="news-footer">
    <div class="news-tags"><span class="news-tag">Knowledge Graphs</span><span class="news-tag">RAG</span><span class="news-tag">Multi-hop Reasoning</span><span class="news-tag">Hybrid Search</span><span class="news-tag">NLP</span></div>
    <a class="news-read-btn" href="https://www.reddit.com/r/MachineLearning/comments/1u5yyyl/i_built_an_opensource_knowledge_graph_pipeline/" target="_blank" rel="noopener noreferrer">Read&nbsp;more&nbsp;&#8594;</a>
  </div>
</div>

<div class="news-item">
  <div class="news-meta">
    <span class="news-source news-source--reddit">Reddit r/MachineLearning</span>
    <span class="news-date">2026-06-13</span>
  </div>
  <a class="news-title" href="https://www.reddit.com/r/MachineLearning/comments/1u4hy2x/paddleocr_v3v4v5v6_implemented_in_c_with_ncnn_p/" target="_blank" rel="noopener noreferrer">PaddleOCR (v3/v4/v5/v6) implemented in C++ with ncnn [P]</a>
  <p class="news-summary">A developer has released a C++ implementation of PaddleOCR (v3-v6) using the ncnn inference framework. This project aims to simplify deployment by removing the heavy dependencies of the official Paddle C++ runtime while maintaining high performance. It is particularly useful for developers seeking a lightweight, easy-to-integrate OCR solution for edge devices.</p>
  <div class="news-footer">
    <div class="news-tags"><span class="news-tag">PaddleOCR</span><span class="news-tag">ncnn</span><span class="news-tag">C++</span><span class="news-tag">Computer Vision</span><span class="news-tag">Edge AI</span></div>
    <a class="news-read-btn" href="https://www.reddit.com/r/MachineLearning/comments/1u4hy2x/paddleocr_v3v4v5v6_implemented_in_c_with_ncnn_p/" target="_blank" rel="noopener noreferrer">Read&nbsp;more&nbsp;&#8594;</a>
  </div>
</div>

<div class="news-item">
  <div class="news-meta">
    <span class="news-source news-source--reddit">Reddit r/MachineLearning</span>
    <span class="news-date">2026-06-13</span>
  </div>
  <a class="news-title" href="https://www.reddit.com/r/MachineLearning/comments/1u4fc16/derivativefree_neural_network_optimization_mnist/" target="_blank" rel="noopener noreferrer">Derivative-Free Neural Network Optimization: MNIST Case [R]</a>
  <p class="news-summary">Researchers demonstrated a derivative-free optimization method (MDP) that successfully trained a neural network on the MNIST dataset without using backpropagation or gradients. The method outperformed the Adam optimizer in both loss and accuracy across a 25,450-dimensional search space. This highlights the potential for non-gradient-based optimization in high-dimensional neural network training.</p>
  <div class="news-footer">
    <div class="news-tags"><span class="news-tag">Derivative-Free Optimization</span><span class="news-tag">Neural Networks</span><span class="news-tag">MNIST</span><span class="news-tag">Optimization Algorithms</span><span class="news-tag">Backpropagation Alternatives</span></div>
    <a class="news-read-btn" href="https://www.reddit.com/r/MachineLearning/comments/1u4fc16/derivativefree_neural_network_optimization_mnist/" target="_blank" rel="noopener noreferrer">Read&nbsp;more&nbsp;&#8594;</a>
  </div>
</div>

<div class="news-item">
  <div class="news-meta">
    <span class="news-source news-source--reddit">Reddit r/DeepLearning</span>
    <span class="news-date">2026-06-15</span>
  </div>
  <a class="news-title" href="https://www.reddit.com/r/deeplearning/comments/1u61dxc/beyond_transformers_why_artificial_life_needs/" target="_blank" rel="noopener noreferrer">Beyond Transformers: Why Artificial Life Needs Physics, Not Just Data</a>
  <p class="news-summary">The post argues that achieving true artificial life requires moving beyond pure data-driven Transformer architectures toward models integrated with physical principles. It suggests that grounding AI in physics is essential for developing autonomous agents that can interact meaningfully with the real world. The discussion highlights the limitations of current LLMs in understanding causality and physical constraints.</p>
  <div class="news-footer">
    <div class="news-tags"><span class="news-tag">Artificial Life</span><span class="news-tag">Transformers</span><span class="news-tag">Robotics</span><span class="news-tag">AI Theory</span><span class="news-tag">Physics-Informed AI</span></div>
    <a class="news-read-btn" href="https://www.reddit.com/r/deeplearning/comments/1u61dxc/beyond_transformers_why_artificial_life_needs/" target="_blank" rel="noopener noreferrer">Read&nbsp;more&nbsp;&#8594;</a>
  </div>
</div>


<h2 id="repos">Trending Repos</h2>
<p class="section-desc">Top repositories this week, sorted by stars.</p>

<div class="weekly-repo-list">

<div class="weekly-repo-item">
  <div class="weekly-repo-header">
    <span class="weekly-rank">#1</span>
    <a class="gh-repo-link" href="https://github.com/AUTOMATIC1111/stable-diffusion-webui" target="_blank" rel="noopener noreferrer">
      <span class="gh-owner">AUTOMATIC1111</span><span class="gh-sep">/</span><strong class="gh-repo">stable-diffusion-webui</strong>
    </a>
    <span class="gh-topic-pill">Computer Vision</span>
    <span class="weekly-stars">&#9733; 163.7k</span>
  </div>
  <p class="gh-summary">This is the most popular web interface for Stable Diffusion, a leading latent diffusion model for image generation. It is highly relevant for research into generative models, multimodal learning, and the practical application of diffusion techniques in computer vision.</p>
  <div class="gh-tags"><span class="gh-tag">diffusion</span><span class="gh-tag">generative models</span><span class="gh-tag">computer vision</span><span class="gh-tag">image generation</span></div>
</div>

<div class="weekly-repo-item">
  <div class="weekly-repo-header">
    <span class="weekly-rank">#2</span>
    <a class="gh-repo-link" href="https://github.com/OpenHands/OpenHands" target="_blank" rel="noopener noreferrer">
      <span class="gh-owner">OpenHands</span><span class="gh-sep">/</span><strong class="gh-repo">OpenHands</strong>
    </a>
    <span class="gh-topic-pill">Agentic AI</span>
    <span class="weekly-stars">&#9733; 77.1k</span>
  </div>
  <p class="gh-summary">OpenHands is an open-source platform for AI-driven software engineering that enables agents to interact with development environments. It is highly relevant as it implements complex multi-agent workflows and autonomous task execution using large language models.</p>
  <div class="gh-tags"><span class="gh-tag">Agentic AI</span><span class="gh-tag">LLM</span><span class="gh-tag">Multi-Agent Systems</span><span class="gh-tag">Software Engineering</span></div>
</div>

<div class="weekly-repo-item">
  <div class="weekly-repo-header">
    <span class="weekly-rank">#3</span>
    <a class="gh-repo-link" href="https://github.com/OpenBB-finance/OpenBB" target="_blank" rel="noopener noreferrer">
      <span class="gh-owner">OpenBB-finance</span><span class="gh-sep">/</span><strong class="gh-repo">OpenBB</strong>
    </a>
    <span class="gh-topic-pill">Agentic AI</span>
    <span class="weekly-stars">&#9733; 69.2k</span>
  </div>
  <p class="gh-summary">OpenBB is a comprehensive financial data platform that provides structured data and tools for analysts and quantitative researchers. It is highly relevant for Agentic AI as it serves as a foundational data layer for building autonomous financial agents and LLM-powered trading systems.</p>
  <div class="gh-tags"><span class="gh-tag">financial data</span><span class="gh-tag">quantitative analysis</span><span class="gh-tag">agentic AI</span><span class="gh-tag">data platform</span></div>
</div>

<div class="weekly-repo-item">
  <div class="weekly-repo-header">
    <span class="weekly-rank">#4</span>
    <a class="gh-repo-link" href="https://github.com/pathwaycom/llm-app" target="_blank" rel="noopener noreferrer">
      <span class="gh-owner">pathwaycom</span><span class="gh-sep">/</span><strong class="gh-repo">llm-app</strong>
    </a>
    <span class="gh-topic-pill">MLOps</span>
    <span class="weekly-stars">&#9733; 59.3k</span>
  </div>
  <p class="gh-summary">This repository provides production-ready cloud templates for RAG and AI pipelines, focusing on synchronizing live data from various enterprise sources. It is highly relevant for MLOps and Agentic AI as it addresses the infrastructure challenges of maintaining real-time data for LLM applications.</p>
  <div class="gh-tags"><span class="gh-tag">RAG</span><span class="gh-tag">MLOps</span><span class="gh-tag">LLM</span><span class="gh-tag">Data Pipelines</span></div>
</div>

<div class="weekly-repo-item">
  <div class="weekly-repo-header">
    <span class="weekly-rank">#5</span>
    <a class="gh-repo-link" href="https://github.com/microsoft/AI-For-Beginners" target="_blank" rel="noopener noreferrer">
      <span class="gh-owner">microsoft</span><span class="gh-sep">/</span><strong class="gh-repo">AI-For-Beginners</strong>
    </a>
    <span class="gh-topic-pill">General</span>
    <span class="weekly-stars">&#9733; 48.1k</span>
  </div>
  <p class="gh-summary">This repository provides a comprehensive 12-week curriculum covering the fundamentals of AI and machine learning. While it is a foundational educational resource rather than a specialized research project, it covers the core concepts necessary to understand the user&#x27;s broader interests in LLMs and Agentic AI.</p>
  <div class="gh-tags"><span class="gh-tag">education</span><span class="gh-tag">machine learning</span><span class="gh-tag">fundamentals</span><span class="gh-tag">deep learning</span></div>
</div>

<div class="weekly-repo-item">
  <div class="weekly-repo-header">
    <span class="weekly-rank">#6</span>
    <a class="gh-repo-link" href="https://github.com/cheahjs/free-llm-api-resources" target="_blank" rel="noopener noreferrer">
      <span class="gh-owner">cheahjs</span><span class="gh-sep">/</span><strong class="gh-repo">free-llm-api-resources</strong>
    </a>
    <span class="gh-topic-pill">LLM</span>
    <span class="weekly-stars">&#9733; 23.5k</span>
  </div>
  <p class="gh-summary">This repository provides a curated list of free LLM inference APIs, which is essential for developers building agentic systems and RAG applications. It serves as a foundational resource for accessing the large language models that power the user&#x27;s interests in multi-agent systems and chatbots.</p>
  <div class="gh-tags"><span class="gh-tag">LLM</span><span class="gh-tag">API</span><span class="gh-tag">Foundation Models</span><span class="gh-tag">Agents</span></div>
</div>

<div class="weekly-repo-item">
  <div class="weekly-repo-header">
    <span class="weekly-rank">#7</span>
    <a class="gh-repo-link" href="https://github.com/mikeroyal/Self-Hosting-Guide" target="_blank" rel="noopener noreferrer">
      <span class="gh-owner">mikeroyal</span><span class="gh-sep">/</span><strong class="gh-repo">Self-Hosting-Guide</strong>
    </a>
    <span class="gh-topic-pill">MLOps</span>
    <span class="weekly-stars">&#9733; 21.3k</span>
  </div>
  <p class="gh-summary">This repository provides a comprehensive guide for self-hosting software, including infrastructure for hosting LLMs and private web servers. It is relevant for MLOps and infrastructure setup, specifically for users looking to deploy models on-premises or in private clouds.</p>
  <div class="gh-tags"><span class="gh-tag">self-hosting</span><span class="gh-tag">infrastructure</span><span class="gh-tag">LLM deployment</span><span class="gh-tag">MLOps</span></div>
</div>

<div class="weekly-repo-item">
  <div class="weekly-repo-header">
    <span class="weekly-rank">#8</span>
    <a class="gh-repo-link" href="https://github.com/lyogavin/airllm" target="_blank" rel="noopener noreferrer">
      <span class="gh-owner">lyogavin</span><span class="gh-sep">/</span><strong class="gh-repo">airllm</strong>
    </a>
    <span class="gh-topic-pill">LLM</span>
    <span class="weekly-stars">&#9733; 20.0k</span>
  </div>
  <p class="gh-summary">This repository provides a method for running a 70B parameter Large Language Model on a single 4GB GPU. It is highly relevant for users interested in efficient inference, model optimization, and making large-scale foundation models accessible on consumer hardware.</p>
  <div class="gh-tags"><span class="gh-tag">LLM</span><span class="gh-tag">inference</span><span class="gh-tag">model optimization</span><span class="gh-tag">quantization</span></div>
</div>

<div class="weekly-repo-item">
  <div class="weekly-repo-header">
    <span class="weekly-rank">#9</span>
    <a class="gh-repo-link" href="https://github.com/trycua/cua" target="_blank" rel="noopener noreferrer">
      <span class="gh-owner">trycua</span><span class="gh-sep">/</span><strong class="gh-repo">cua</strong>
    </a>
    <span class="gh-topic-pill">Agentic AI</span>
    <span class="weekly-stars">&#9733; 18.3k</span>
  </div>
  <p class="gh-summary">This repository provides the core infrastructure for Computer-Use Agents, enabling AI to interact with full desktop environments across multiple operating systems. It is highly relevant as it provides the sandboxing, SDKs, and benchmarks necessary for developing and evaluating autonomous agents in human-computer interaction scenarios.</p>
  <div class="gh-tags"><span class="gh-tag">Computer-Use</span><span class="gh-tag">Agentic AI</span><span class="gh-tag">Human-Computer Interaction</span><span class="gh-tag">Sandboxing</span></div>
</div>

<div class="weekly-repo-item">
  <div class="weekly-repo-header">
    <span class="weekly-rank">#10</span>
    <a class="gh-repo-link" href="https://github.com/andrewyng/aisuite" target="_blank" rel="noopener noreferrer">
      <span class="gh-owner">andrewyng</span><span class="gh-sep">/</span><strong class="gh-repo">aisuite</strong>
    </a>
    <span class="gh-topic-pill">Agentic AI</span>
    <span class="weekly-stars">&#9733; 14.5k</span>
  </div>
  <p class="gh-summary">This repository provides a unified interface to interact with multiple Generative AI providers, simplifying the integration of various LLMs into applications. It is highly relevant for building Agentic AI systems and multi-agent workflows by abstracting the complexity of different model APIs.</p>
  <div class="gh-tags"><span class="gh-tag">LLM</span><span class="gh-tag">Agentic AI</span><span class="gh-tag">Generative AI</span><span class="gh-tag">Python</span></div>
</div>

</div>
