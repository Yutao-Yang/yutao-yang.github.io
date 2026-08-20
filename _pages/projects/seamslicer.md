---
permalink: /projects/seamslicer/
title: "SeamSlicer & AtomicBench"
layout: single
author_profile: false
classes: wide
---

<article class="project-page">
  <a class="project-back" href="/#projects">← Back to projects</a>
  <header class="project-hero"><p class="project-kicker">MULTIMODAL VIDEO SLICING · SEP. 2025 — MAY 2026</p><h1>SeamSlicer &amp; AtomicBench</h1><p class="project-deck">Speech-aware boundary reasoning for semantically complete, atomic-level automated video trimming.</p><div class="project-tags"><span class="tag-blue">Multimodal Learning</span><span class="tag-gray">Temporal Boundary Detection</span></div><img src="/assets/images/projects/seamslicer-hero.webp" alt="Conceptual overview of speech-aware multimodal video slicing"></header>

  <section class="project-overview"><div><strong>Role</strong><span>Second author</span></div><div><strong>Venue</strong><span>ACM Multimedia 2026 · Accepted</span></div><div><strong>Core task</strong><span>Atomic-level boundary detection</span></div><div><strong>Benchmark</strong><span>AtomicBench</span></div></section>

  <section class="project-section"><h2>Why atomic slicing?</h2><div class="project-copy"><p>Fixed-duration cuts can break dialogue, while purely visual boundaries may ignore narration or multi-speaker exchanges. Coarse scene segmentation also leaves unnecessary material inside clips. SeamSlicer treats a useful editing unit as both visually continuous and semantically complete.</p><p>The method jointly reasons over visual continuity, narration, dialogue, music, sound effects, on-screen text, and ambient audio.</p></div></section>

  <section class="project-section"><h2>Three-stage method</h2><div class="process-grid three"><div><b>01</b><h3>Boundary extraction</h3><p>Combine visual boundary evidence with source-separated audio and timestamped speech intervals.</p></div><div><b>02</b><h3>Visual refinement</h3><p>Refine candidate cuts using learned temporal features, RGB histogram similarity, and inter-frame similarity.</p></div><div><b>03</b><h3>Length control</h3><p>Preserve speech-complete segments and subdivide long silent spans using secondary cues.</p></div></div></section>

  <section class="project-section"><h2>Boundary reasoning</h2><div class="equation-card"><p>A visual boundary is accepted only when it does not interrupt a detected speech interval:</p><div class="formula">B<sub>final</sub> = { b ∈ B<sub>visual</sub> | b ∉ [t<sub>s</sub>, t<sub>e</sub>] for every speech interval [t<sub>s</sub>, t<sub>e</sub>] }.</div><p>For a long silent segment of duration <i>d</i><sub>i</sub>, uniform subdivision is used only as a fallback: <i>m</i> = ⌈<i>d</i><sub>i</sub> / <i>τ</i>⌉, with <i>τ</i> = 6 seconds and <i>d</i><sub>sub</sub> = <i>d</i><sub>i</sub> / <i>m</i>.</p></div></section>

  <section class="project-section"><h2>My contribution</h2><ul class="contribution-list"><li>Participated in candidate-boundary extraction and visual-boundary refinement.</li><li>Contributed to the multi-strategy length-control design.</li><li>Participated in AtomicBench construction, experiments, analysis, and paper preparation.</li></ul></section>

  <section class="project-section"><h2>Verified evaluation</h2><div class="evidence-grid"><div><strong>15,779</strong><span>boundary annotations</span></div><div><strong>100</strong><span>videos in AtomicBench</span></div><div><strong>≈1,000 min</strong><span>annotated video duration</span></div><div><strong>0.837</strong><span>F1 on AtomicBench</span></div></div><p class="project-note">Reported in the accepted paper. AtomicBench contains segments mainly spanning 1–15 seconds; the paper also reports evaluation on BBC and RAI and a human study on trimmed-video quality.</p></section>

  <section class="project-result"><p class="project-kicker">PUBLICATION</p><h2>Accepted at ACM Multimedia 2026</h2><p><strong>Speech-Aware Multimodal Video Slicing for Automated Video Trimming</strong><br>Yandong Liu, <strong>Yutao Yang</strong>, Shengjiao Dong, Wenqiang Zhang, Xiang Li, Mengli Yu, Zhao-Min Chen, and Lingfeng Yang.</p></section>
  <nav class="project-next"><a href="/projects/surveillance-anomaly-detection/">Next project: Surveillance Anomaly Detection →</a></nav>
</article>
