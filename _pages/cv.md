---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

Education
======
* Ph.D in Computer Science, Nankai University & Zhongguancun Academy, 2025 (expected)
* B.S. in Software Engineering, Shanxi University, 2025

Work experience
======
* Research Interests: Computer Vision, Embodied AI, World Models

Skills
======
* Programming: Python, PyTorch, C++
* Computer Vision: Deep Learning, Image Processing
* Embodied AI: Reinforcement Learning, Robotics

Interests
======
* Calligraphy (Shou Jin Ti - Song Dynasty Style)

Publications
======
  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
Talks
======
  <ul>{% for post in site.talks reversed %}
    {% include archive-single-talk-cv.html  %}
  {% endfor %}</ul>
  
Teaching
======
  <ul>{% for post in site.teaching reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
