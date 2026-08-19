---
permalink: /projects/lumensport/
title: "LumenSport"
layout: single
author_profile: false
classes: wide
---

<article class="project-page">
  <a class="project-back" href="/#projects">← Back to projects</a>
  <header class="project-hero">
    <p class="project-kicker">SPORTS VIDEO INTELLIGENCE · SEP. 2025 — MAY 2026</p>
    <h1>LumenSport</h1>
    <p class="project-deck">An end-to-end system that turns raw sports footage into structured analysis and editable video narratives.</p>
    <div class="project-tags"><span>Video Understanding</span><span>Multimodal Analysis</span><span>Automated Editing</span><span>Football &amp; Basketball</span></div>
    <img src="/assets/images/projects/lumensport-hero.webp" alt="Conceptual overview of the LumenSport sports-video analysis and editing pipeline">
  </header>

  <section class="project-overview">
    <div><strong>Role</strong><span>Project lead · Lead developer</span></div>
    <div><strong>Scope</strong><span>System architecture, models, backend, and interface</span></div>
    <div><strong>Outcome</strong><span>National First Prize–associated football platform</span></div>
    <div><strong>Resource</strong><span><a href="https://github.com/Yutao-Yang/LumenSport">Public GitHub repository ↗</a></span></div>
  </section>

  <section class="project-section"><h2>Problem</h2><div class="project-copy"><p>Long sports videos contain many different temporal structures: rallies, possessions, tactical events, individual actions, and emotionally salient highlights. A useful editing system must therefore do more than detect shots—it must interpret the sport, locate meaningful units, preserve temporal context, and assemble clips around a clear editorial intent.</p><p>LumenSport organizes these requirements as a layered workflow instead of relying on a single model to make every decision.</p></div></section>

  <section class="project-section"><h2>System pipeline</h2><div class="process-grid">
    <div><b>01</b><h3>Classify</h3><p>Identify the sport and select sport-specific processing logic.</p></div>
    <div><b>02</b><h3>Segment</h3><p>Split long footage into rounds, rallies, possessions, or action units.</p></div>
    <div><b>03</b><h3>Understand</h3><p>Evaluate highlights, tactical events, and player-centric moments.</p></div>
    <div><b>04</b><h3>Orchestrate</h3><p>Arrange selected material using one of eight editing narratives.</p></div>
  </div></section>

  <section class="project-section"><h2>Technical design</h2><div class="project-columns"><div><h3>Perception and temporal modeling</h3><p>The repository integrates Swin Transformer for sport/scene classification, SlowFast for round or action segmentation, ConvNeXtV2 for in-round event assessment, VideoMAE for football action recognition, and YOLO with ByteTrack for player detection and tracking.</p></div><div><h3>Editing intelligence</h3><p>The orchestrator supports highlight, funny, tactical, technical, comparison, knowledge, match-replay, and training narratives. These modes provide explicit editorial objectives for selecting and arranging candidate clips.</p></div><div><h3>Engineering</h3><p>I built the Python processing backend and a React, Vite, and TypeScript interface. The repository separates video processing, orchestration, player highlights, model utilities, storage integration, and frontend modules.</p></div></div></section>

  <section class="project-section"><h2>My contribution</h2><ul class="contribution-list"><li>Led the system architecture and primary implementation.</li><li>Designed sport classification, temporal segmentation, highlight scoring, tactical analysis, player tracking, and reel-generation stages.</li><li>Integrated heterogeneous video, detection, tracking, and multimodal components into one workflow.</li><li>Implemented the backend and the editor/analytics-oriented web interface.</li></ul></section>

  <section class="project-result"><p class="project-kicker">VERIFIED OUTCOME</p><h2>From research prototype to competition work</h2><p>The associated “Yuelai Sports · Intelligent Football Platform” received <strong>First Prize</strong> in the Football Application Innovation Track at the First National Football AI Innovation Exchange Conference.</p><p class="project-note">No additional accuracy, latency, deployment-scale, or user-impact claims are presented because they are not verified in the current project record.</p></section>
  <nav class="project-next"><a href="/projects/seamslicer/">Next project: SeamSlicer →</a></nav>
</article>
