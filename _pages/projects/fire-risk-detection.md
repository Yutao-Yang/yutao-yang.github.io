---
permalink: /projects/fire-risk-detection/
title: "Fire & Smoke Detection"
layout: single
author_profile: false
classes: wide
---

<article class="project-page">
  <a class="project-back" href="/#projects">← Back to projects</a>
  <header class="project-hero"><p class="project-kicker">OBJECT DETECTION · MAR. 2023 — SEP. 2024</p><h1>Fire &amp; Smoke Detection</h1><p class="project-deck">A YOLOv8-based detector designed around diffuse smoke, occluded targets, and small flames.</p><div class="project-tags"><span class="tag-orange">Object Detection</span><span class="tag-green">AI for Safety</span></div><img src="/assets/images/projects/fire-risk-hero.webp" alt="Conceptual multi-scale fire and smoke detection architecture"></header>
  <section class="project-overview"><div><strong>Role</strong><span>Project lead</span></div><div><strong>Data</strong><span>Self-constructed project dataset</span></div><div><strong>Verified result</strong><span>91.8% mAP</span></div><div><strong>Focus</strong><span>Smoke, occlusion, and small flames</span></div></section>
  <section class="project-section"><h2>Problem</h2><div class="project-copy"><p>Fire-risk imagery spans very different visual scales. Smoke has diffuse boundaries, flames may occupy only a few pixels, and partial occlusion can hide decisive cues. The project therefore emphasized receptive-field diversity and selective feature fusion rather than treating all feature levels equally.</p></div></section>
  <section class="project-section"><h2>Architecture</h2><div class="process-grid three"><div><b>01</b><h3>Multi-scale context</h3><p>Parallel dilated convolution captures local details and broader smoke structure.</p></div><div><b>02</b><h3>Collaborative attention</h3><p>MCA-style attention strengthens informative channels and spatial regions.</p></div><div><b>03</b><h3>Feature selection</h3><p>A coordinate-attention-guided hierarchical pyramid filters and fuses features across levels.</p></div></div></section>
  <section class="project-section"><h2>Design intuition</h2><div class="equation-card"><p>Parallel dilation expands context without requiring a single oversized kernel:</p><div class="formula"><i>F</i><sub>multi</sub> = Concat(Conv<sub>r₁</sub>(<i>F</i>), Conv<sub>r₂</sub>(<i>F</i>), …).</div><p>Attention weights then modulate hierarchical features before detection. The equation describes the architectural idea and does not add unverified performance claims.</p></div></section>
  <section class="project-section"><h2>My contribution</h2><ul class="contribution-list"><li>Led the project and organized the detector development around YOLOv8.</li><li>Designed the parallel dilated-convolution, MCA-attention, and coordinate-attention-guided feature-pyramid components.</li><li>Focused the model design on smoke diffusion, partial occlusion, and small-flame detection.</li><li>Constructed and evaluated the project dataset.</li></ul></section>
  <section class="project-result"><p class="project-kicker">VERIFIED RESULT</p><h2>91.8% mAP on the project dataset</h2><p>The current record also documents gains of approximately 0.5–0.6 percentage points in occluded-target recall and 1.7 percentage points in small-flame accuracy. No real-world deployment claim is made.</p></section>
  <nav class="project-next"><a href="/projects/makeupvision/">Next project: MakeupVision →</a></nav>
</article>
