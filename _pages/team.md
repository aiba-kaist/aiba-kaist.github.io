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
<div class="row mb-4">
  <div class="col-sm-3">
    <img class="img-fluid rounded" src="/assets/img/members/{{ m.photo }}" alt="{{ m.name_en }}">
  </div>
  <div class="col-sm-9">
    <h4>{{ m.name_en }}</h4>
    <p>{{ m.position }}<br>
    {{ m.affiliation }}<br></p>
    
    <p><strong>Email:</strong> {{ m.email }}</p>
    <p><strong>Office:</strong> {{ m.office }}</p>
    <p><strong>Tel:</strong> {{ m.phone }}</p>
    
    {% if m.bio %}
    {% assign bio_paragraphs = m.bio | split: "\n\n" %}
    {% for para in bio_paragraphs %}
    <p style="text-align:justify;">{{ para }}</p>
    {% endfor %}
    {% endif %}
  </div>

  <div class="col-sm-auto">
  {% if m.education %}
  <p><strong>Education:</strong> {{ m.education }}</p>
  {% endif %}
  
  {% if m.career %}
  <strong>Experience:</strong>
  <ul>
    {% assign career_lines = m.career | split: "|" %}
    {% for line in career_lines %}
    {% if line != "" %}<li>{{ line }}</li>{% endif %}
    {% endfor %}
  </ul>
  {% endif %}
  </div>
</div>
{% endfor %}

---
{% endif %}

{% if phd.size > 0 %}
## Ph.D. Students

<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:2rem;margin-top:1.5rem;">
{% for m in phd %}
  <div style="text-align:center;">
    <img class="rounded" src="/assets/img/members/{{ m.photo }}" alt="{{ m.name_en }}" style="width:140px;height:140px;object-fit:cover;object-position:top;">
    <h5 style="margin-top:0.5rem;margin-bottom:0.25rem;">{{ m.name_en }}</h5>
    <p style="color:#6c757d;margin:0;">{{ m.research_area }}</p>
  </div>
{% endfor %}
</div>

---
{% endif %}

{% if ms.size > 0 %}
## M.S. Students

<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:2rem;margin-top:1.5rem;">
{% for m in ms %}
  <div style="text-align:center;">
    <img class="rounded" src="/assets/img/members/{{ m.photo }}" alt="{{ m.name_en }}" style="width:140px;height:140px;object-fit:cover;object-position:top;">
    <h5 style="margin-top:0.5rem;margin-bottom:0.25rem;">{{ m.name_en }}</h5>
    <p style="color:#6c757d;margin:0;">{{ m.research_area }}</p>
  </div>
{% endfor %}
</div>

---
{% endif %}

{% if undergrad.size > 0 %}
## Undergraduate Researcher

<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:2rem;margin-top:1.5rem;">
{% for m in undergrad %}
  <div style="text-align:center;">
    <img class="rounded" src="/assets/img/members/{{ m.photo }}" alt="{{ m.name_en }}" style="width:140px;height:140px;object-fit:cover;object-position:top;">
    <h5 style="margin-top:0.5rem;margin-bottom:0.25rem;">{{ m.name_en }}</h5>
    <p style="color:#6c757d;margin:0;">{{ m.research_area }}</p>
  </div>
{% endfor %}
</div>

---
{% endif %}

{% if alumni.size > 0 %}
## Alumni

<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:2rem;margin-top:1.5rem;">
{% for m in alumni %}
  <div style="text-align:center;">
    <img class="rounded" src="/assets/img/members/{{ m.photo }}" alt="{{ m.name_en }}" style="width:140px;height:140px;object-fit:cover;object-position:top;">
    <h5 style="margin-top:0.5rem;margin-bottom:0.25rem;">{{ m.name_en }}</h5>
    <p style="color:#6c757d;margin:0;">{{ m.graduation_info }}</p>
  </div>
{% endfor %}
</div>
{% endif %}

{% else %}

<!-- Fallback -->

## Faculty

<div class="row mb-4">
  <div class="col-sm-3">
    <img class="img-fluid rounded" src="/assets/img/members/shin.jpg" alt="Donghyuk Shin">
  </div>
  <div class="col-sm-9">
    <h4>Donghyuk Shin</h4>
    <p><strong>Associate Professor</strong><br>
    KAIST College of Business (School of Management Engineering)<br>
    <a href="mailto:dhs@kaist.ac.kr">dhs@kaist.ac.kr</a> · <a href="https://dshin32.github.io">Personal Website</a></p>
    
    <p style="text-align:justify;">I am an Associate Professor in the College of Business (School of Management Engineering) at the Korea Advanced Institute of Science and Technology (KAIST). My research interests lie at the intersection of machine learning (ML) and information systems. Topics of interest include but are not limited to artificial intelligence, digital platforms, educational technology, and their business and societal impacts. In my research, I use ML, econometric analysis, and randomized field experiments.</p>
    
    <p style="text-align:justify;">Prior to joining KAIST, I was an Assistant Professor of Information Systems at the W. P. Carey School of Business, Arizona State University (2019–2024). Before that, I served as a Machine Learning Scientist at Amazon Web Services (2016–2019), where I developed and implemented ML systems to understand and serve customer needs on the world's largest Cloud platform. I obtained my Ph.D. in Computer Science from the University of Texas at Austin under the supervision of Prof. Inderjit S. Dhillon. During my graduate studies, I had also closely worked with Prof. Andrew B. Whinston and spent time at Yahoo! Research (2014) and Amazon (2013).</p>
    
    <p><strong>Research Areas:</strong> Artificial Intelligence, Economics of AI and IT, AI/ML Applications, Digital Platforms</p>
    
    <p><strong>Education:</strong> Ph.D. in Computer Science, The University of Texas at Austin</p>
    
    <p><strong>Career:</strong></p>
    <ul>
      <li>Associate Professor, KAIST (2024~Present)</li>
      <li>Assistant Professor, Arizona State University (2019~2024)</li>
      <li>Machine Learning Scientist, Amazon Web Services (2016~2019)</li>
    </ul>
    
    <p><strong>Industry Advisory:</strong> POSCO Holdings Inc. (N.EX.T Hub, AI Lab), AI Advisory Council, 2024</p>
  </div>
</div>

---

## Ph.D. Students

<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:2rem;margin-top:1.5rem;">
  <div style="text-align:center;">
    <img class="rounded" src="/assets/img/members/park_jaehyung.jpg" alt="Junhoe Park" style="width:140px;height:140px;object-fit:cover;object-position:top;">
    <h5 style="margin-top:0.5rem;margin-bottom:0.25rem;">Junhoe Park</h5>
    <p style="color:#6c757d;margin:0;">IT/AI</p>
  </div>
  <div style="text-align:center;">
    <img class="rounded" src="/assets/img/members/baek_junha.png" alt="Junha Baek" style="width:140px;height:140px;object-fit:cover;object-position:top;">
    <h5 style="margin-top:0.5rem;margin-bottom:0.25rem;">Junha Baek</h5>
    <p style="color:#6c757d;margin:0;">Generative AI</p>
  </div>
  <div style="text-align:center;">
    <img class="rounded" src="/assets/img/members/kim_gaon.jpg" alt="Gaon Kim" style="width:140px;height:140px;object-fit:cover;object-position:top;">
    <h5 style="margin-top:0.5rem;margin-bottom:0.25rem;">Gaon Kim</h5>
    <p style="color:#6c757d;margin:0;">Financial AI</p>
  </div>
  <div style="text-align:center;">
    <img class="rounded" src="/assets/img/members/yoo_youngjun.png" alt="Youngjun Yu" style="width:140px;height:140px;object-fit:cover;object-position:top;">
    <h5 style="margin-top:0.5rem;margin-bottom:0.25rem;">Youngjun Yu</h5>
    <p style="color:#6c757d;margin:0;">IT/AI</p>
  </div>
  <div style="text-align:center;">
    <img class="rounded" src="/assets/img/members/ahn_taehyun.png" alt="Taehyun Ahn" style="width:140px;height:140px;object-fit:cover;object-position:top;">
    <h5 style="margin-top:0.5rem;margin-bottom:0.25rem;">Taehyun Ahn</h5>
    <p style="color:#6c757d;margin:0;">AI Agent</p>
  </div>
  <div style="text-align:center;">
    <img class="rounded" src="/assets/img/members/kim_seohyun.png" alt="Seohyun Kim" style="width:140px;height:140px;object-fit:cover;object-position:top;">
    <h5 style="margin-top:0.5rem;margin-bottom:0.25rem;">Seohyun Kim</h5>
    <p style="color:#6c757d;margin:0;">Healthcare AI</p>
  </div>
  <div style="text-align:center;">
    <img class="rounded" src="/assets/img/members/lee_suhyeon.png" alt="Suhyeon Lee" style="width:140px;height:140px;object-fit:cover;object-position:top;">
    <h5 style="margin-top:0.5rem;margin-bottom:0.25rem;">Suhyeon Lee</h5>
    <p style="color:#6c757d;margin:0;">LLM</p>
  </div>
</div>

---

## M.S. Students

<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:2rem;margin-top:1.5rem;">
  <div style="text-align:center;">
    <img class="rounded" src="/assets/img/members/park_woohyun.png" alt="Woohyun Park" style="width:140px;height:140px;object-fit:cover;object-position:top;">
    <h5 style="margin-top:0.5rem;margin-bottom:0.25rem;">Woohyun Park</h5>
    <p style="color:#6c757d;margin:0;">Platform</p>
  </div>
</div>

---

## Undergraduate Researcher

<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:2rem;margin-top:1.5rem;">
  <div style="text-align:center;">
    <img class="rounded" src="/assets/img/members/seo_yeonwoo.jpg" alt="Yeonwoo Seo" style="width:140px;height:140px;object-fit:cover;object-position:top;">
    <h5 style="margin-top:0.5rem;margin-bottom:0.25rem;">Yeonwoo Seo</h5>
    <p style="color:#6c757d;margin:0;">Causal ML</p>
  </div>
</div>

---

## Alumni

<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:2rem;margin-top:1.5rem;">
  <div style="text-align:center;">
    <img class="rounded" src="/assets/img/members/yoo_woojeong.png" alt="Woojeong Yoo" style="width:140px;height:140px;object-fit:cover;object-position:top;">
    <h5 style="margin-top:0.5rem;margin-bottom:0.25rem;">Woojeong Yoo</h5>
    <p style="color:#6c757d;margin:0;">M.S. 2025 · PwC</p>
  </div>
</div>

{% endif %}
