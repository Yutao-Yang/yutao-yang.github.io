---
permalink: /projects/makeupvision/
title: "MakeupVision"
layout: single
author_profile: false
classes: wide
---

<article class="project-page">
  <a class="project-back" href="/#projects">← Back to projects</a>
  <header class="project-hero"><p class="project-kicker">FACIAL ANALYSIS · MAY 2024 — MAY 2025</p><h1>MakeupVision</h1><p class="project-deck">A virtual-makeup vision pipeline combining face detection, dense landmarks, semantic facial regions, and localized texture transfer.</p><div class="project-tags"><span>Face Detection</span><span>106-point Landmarks</span><span>Semantic Segmentation</span><span>Texture Transfer</span></div><img src="/assets/images/projects/makeupvision-hero.webp" alt="Conceptual computer-vision pipeline for virtual makeup"></header>
  <section class="project-overview"><div><strong>Role</strong><span>Project lead</span></div><div><strong>Program</strong><span>Shanxi University Innovation Training</span></div><div><strong>Completion</strong><span>Rated Good</span></div><div><strong>Focus</strong><span>Precise facial-region localization</span></div></section>
  <section class="project-section"><h2>Problem</h2><div class="project-copy"><p>Virtual makeup requires more than global image stylization. The system must locate a face, understand facial geometry, isolate semantic regions, and transfer texture without bleeding across boundaries such as lips, eyelids, brows, and surrounding skin.</p></div></section>
  <section class="project-section"><h2>Pipeline</h2><div class="process-grid"><div><b>01</b><h3>Detect</h3><p>Light-FaceDetector locates the face and defines the working region.</p></div><div><b>02</b><h3>Align</h3><p>A 106-point landmark heatmap model estimates dense facial geometry.</p></div><div><b>03</b><h3>Parse</h3><p>Makeup-master semantic segmentation separates facial regions.</p></div><div><b>04</b><h3>Transfer</h3><p>Region-aware masks guide localized cross-layer texture transfer.</p></div></div></section>
  <section class="project-section"><h2>Technical focus</h2><div class="project-columns"><div><h3>ROI localization</h3><p>Landmarks and semantic labels provide stable regions of interest for the lips, eyes, and other cosmetic areas.</p></div><div><h3>Mask construction</h3><p>Lip and eye-region masks constrain each operation to the intended facial structure.</p></div><div><h3>Texture propagation</h3><p>Cross-layer feature transfer connects source appearance information with spatially aligned target regions.</p></div></div></section>
  <section class="project-section"><h2>My contribution</h2><ul class="contribution-list"><li>Led the student innovation project and integrated the main vision modules.</li><li>Implemented ROI localization and region-specific mask generation.</li><li>Worked on cross-layer texture-feature transfer for localized virtual makeup.</li><li>Coordinated project completion and documentation.</li></ul></section>
  <section class="project-result"><p class="project-kicker">VERIFIED OUTCOME</p><h2>University innovation project · Completion rated Good</h2><p>No public repository, quantitative benchmark, released dataset, or deployment result is listed because none is verified in the current project record.</p></section>
  <nav class="project-next"><a href="/projects/lumensport/">Return to LumenSport →</a></nav>
</article>
