---
layout: page
permalink: /teaching/
title: teaching
description: Courses taught by Prof. Shin
nav: true
nav_order: 6
---

{% assign teaching_data = site.data.admin_data.teaching %}

{% if teaching_data %}

{% assign current = teaching_data | where: "is_current", true %}
{% assign past = teaching_data | where: "is_current", false %}

## Current Courses

### KAIST
(All courses are graduate-level unless otherwise noted.)

{% for c in current %}
##### [{{ c.course_code }}] {{ c.course_name }}
{% if c.topics %}- Topics: {{ c.topics }}{% endif %}

{% endfor %}

---

## Past Courses

{% for c in past %}
- {{ c.course_name }}{% if c.semester %} ({{ c.semester }}){% endif %}
{% endfor %}

{% else %}

<!-- Fallback: 기존 하드코딩 데이터 -->

## Current Courses

### KAIST Graduate School of Business

**MGT 562 - Business Analytics**
- Graduate level course on data analytics for business decision-making
- Topics: Machine Learning, Deep Learning, NLP, Causal Inference

**MGT 565 - IT and Strategy**  
- Graduate level course on strategic implications of IT
- Topics: Platform Economics, AI/IT Economics, Digital Transformation

---

## Past Courses

- Business Analytics (2023-2024)
- IT and Strategy (2023-2024)
- Data Science for Business (2022-2023)

{% endif %}
