---
layout: page
permalink: /team/
title: team
description: Members of AIBA Lab
nav: true
nav_order: 2
---

{% assign members_data = site.data.admin_data.members %}

{% if members_data %}

{% assign faculty = members_data | where: "role", "Faculty" %}
{% assign phd = members_data | where: "role", "PhD" %}
{% assign ms = members_data | where: "role", "MS" %}
{% assign undergrad = members_data | where: "role", "Undergrad" %}
{% assign alumni = members_data | where: "role", "Alumni" %}

{% if faculty.size > 0 %}
## Faculty

{% for m in faculty %}
<div class="row">
  <div class="col-sm-3">
    <img class="img-fluid rounded" src="/assets/img/members/{{ m.photo }}" alt="{{ m.name_en }}">
  </div>
  <div class="col-sm-9">
    <h4>{{ m.name_en }}</h4>
    <p><strong>{{ m.position }}</strong><br>
    {{ m.affiliation }}<br>
    <a href="mailto:{{ m.email }}">{{ m.email }}</a>{% if m.website %} · 
    <a href="{{ m.website }}">Personal Website</a>{% endif %}</p>
    <p><em>Research Interests:</em> {{ m.research_area }}</p>
    {% if m.bio %}
    <ul>
      {% assign bio_lines = m.bio | split: "\n" %}
      {% for line in bio_lines %}
      {% if line != "" %}<li>{{ line }}</li>{% endif %}
      {% endfor %}
    </ul>
    {% endif %}
  </div>
</div>

---
{% endfor %}
{% endif %}

{% if phd.size > 0 %}
## Ph.D. Students

<div class="row row-cols-2 row-cols-md-4 g-4 mt-3">
{% for m in phd %}
  <div class="col text-center mb-4">
    <img class="img-fluid rounded mb-2" src="/assets/img/members/{{ m.photo }}" alt="{{ m.name_en }}" style="width:150px;height:150px;object-fit:cover;">
    <h5>{{ m.name_en }}</h5>
    <p>{{ m.research_area }}</p>
  </div>
{% endfor %}
</div>

---
{% endif %}

{% if ms.size > 0 %}
## M.S. Students

<div class="row row-cols-2 row-cols-md-4 g-4 mt-3">
{% for m in ms %}
  <div class="col text-center mb-4">
    <img class="img-fluid rounded mb-2" src="/assets/img/members/{{ m.photo }}" alt="{{ m.name_en }}" style="width:150px;height:150px;object-fit:cover;">
    <h5>{{ m.name_en }}</h5>
    <p>{{ m.research_area }}</p>
  </div>
{% endfor %}
</div>

---
{% endif %}

{% if undergrad.size > 0 %}
## Undergraduate Researcher

<div class="row row-cols-2 row-cols-md-4 g-4 mt-3">
{% for m in undergrad %}
  <div class="col text-center mb-4">
    <img class="img-fluid rounded mb-2" src="/assets/img/members/{{ m.photo }}" alt="{{ m.name_en }}" style="width:150px;height:150px;object-fit:cover;">
    <h5>{{ m.name_en }}</h5>
    <p>{{ m.research_area }}</p>
  </div>
{% endfor %}
</div>

---
{% endif %}

{% if alumni.size > 0 %}
## Alumni

<div class="row row-cols-2 row-cols-md-4 g-4 mt-3">
{% for m in alumni %}
  <div class="col text-center mb-4">
    <img class="img-fluid rounded mb-2" src="/assets/img/members/{{ m.photo }}" alt="{{ m.name_en }}" style="width:150px;height:150px;object-fit:cover;">
    <h5>{{ m.name_en }}</h5>
    <p>{{ m.graduation_info }}</p>
  </div>
{% endfor %}
</div>
{% endif %}

{% else %}

<!-- Fallback: 기존 하드코딩 데이터 -->

## Faculty

<div class="row">
  <div class="col-sm-3">
    <img class="img-fluid rounded" src="/assets/img/members/shin.jpg" alt="Donghyuk Shin">
  </div>
  <div class="col-sm-9">
    <h4>Donghyuk Shin</h4>
    <p><strong>Associate Professor</strong><br>
    KAIST College of Business (School of Management Engineering)<br>
    <a href="mailto:dhs@kaist.ac.kr">dhs@kaist.ac.kr</a> · 
    <a href="https://dshin32.github.io">Personal Website</a></p>
    <p><em>Research Interests:</em> Economics of AI/IT, AI/ML Applications, Digital Platforms</p>
    <ul>
      <li>Ph.D. in Computer Science, UT Austin</li>
      <li>Assistant Professor, Arizona State University</li>
      <li>ML Scientist, Amazon</li>
    </ul>
  </div>
</div>

---

## Ph.D. Students

<div class="row row-cols-2 row-cols-md-4 g-4 mt-3">
  <div class="col text-center mb-4">
    <img class="img-fluid rounded mb-2" src="/assets/img/members/park_jaehyung.jpg" alt="Jaehyung Park" style="width:150px;height:150px;object-fit:cover;">
    <h5>Jaehyung Park</h5>
    <p>IT/AI</p>
  </div>
  <div class="col text-center mb-4">
    <img class="img-fluid rounded mb-2" src="/assets/img/members/baek_junha.png" alt="Junha Baek" style="width:150px;height:150px;object-fit:cover;">
    <h5>Junha Baek</h5>
    <p>Generative AI</p>
  </div>
  <div class="col text-center mb-4">
    <img class="img-fluid rounded mb-2" src="/assets/img/members/kim_gaon.jpg" alt="Gaon Kim" style="width:150px;height:150px;object-fit:cover;">
    <h5>Gaon Kim</h5>
    <p>Financial AI</p>
  </div>
  <div class="col text-center mb-4">
    <img class="img-fluid rounded mb-2" src="/assets/img/members/yoo_youngjun.png" alt="Youngjun Yoo" style="width:150px;height:150px;object-fit:cover;">
    <h5>Youngjun Yoo</h5>
    <p>IT/AI</p>
  </div>
  <div class="col text-center mb-4">
    <img class="img-fluid rounded mb-2" src="/assets/img/members/ahn_taehyun.png" alt="Taehyun Ahn" style="width:150px;height:150px;object-fit:cover;">
    <h5>Taehyun Ahn</h5>
    <p>AI Agent</p>
  </div>
  <div class="col text-center mb-4">
    <img class="img-fluid rounded mb-2" src="/assets/img/members/kim_seohyun.png" alt="Seohyun Kim" style="width:150px;height:150px;object-fit:cover;">
    <h5>Seohyun Kim</h5>
    <p>Healthcare AI</p>
  </div>
  <div class="col text-center mb-4">
    <img class="img-fluid rounded mb-2" src="/assets/img/members/lee_suhyeon.png" alt="Suhyeon Lee" style="width:150px;height:150px;object-fit:cover;">
    <h5>Suhyeon Lee</h5>
    <p>LLM</p>
  </div>
</div>

---

## M.S. Students

<div class="row row-cols-2 row-cols-md-4 g-4 mt-3">
  <div class="col text-center mb-4">
    <img class="img-fluid rounded mb-2" src="/assets/img/members/park_woohyun.png" alt="Woohyun Park" style="width:150px;height:150px;object-fit:cover;">
    <h5>Woohyun Park</h5>
    <p>Platform</p>
  </div>
</div>

---

## Undergraduate Researcher

<div class="row row-cols-2 row-cols-md-4 g-4 mt-3">
  <div class="col text-center mb-4">
    <img class="img-fluid rounded mb-2" src="/assets/img/members/seo_yeonwoo.jpg" alt="Yeonwoo Seo" style="width:150px;height:150px;object-fit:cover;">
    <h5>Yeonwoo Seo</h5>
    <p>Causal ML</p>
  </div>
</div>

---

## Alumni

<div class="row row-cols-2 row-cols-md-4 g-4 mt-3">
  <div class="col text-center mb-4">
    <img class="img-fluid rounded mb-2" src="/assets/img/members/yoo_woojeong.png" alt="Woojeong Yoo" style="width:150px;height:150px;object-fit:cover;">
    <h5>Woojeong Yoo</h5>
    <p>M.S. 2025 · PwC</p>
  </div>
</div>

{% endif %}
