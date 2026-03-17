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
    <p><strong>{{ m.position }}</strong><br>
    {{ m.affiliation }}<br>
    <a href="mailto:{{ m.email }}">{{ m.email }}</a>{% if m.website %} · <a href="{{ m.website }}">Personal Website</a>{% endif %}</p>
    
    {% if m.bio %}
    {% assign bio_paragraphs = m.bio | split: "\n\n" %}
    {% for para in bio_paragraphs %}
    <p style="text-align:justify;">{{ para }}</p>
    {% endfor %}
    {% endif %}
    
    <p><strong>Research Areas:</strong> {{ m.research_area }}</p>
    
    {% if m.education %}
    <p><strong>Education:</strong> {{ m.education }}</p>
    {% endif %}
    
    {% if m.career %}
    <p><strong>Career:</strong></p>
    <ul>
      {% assign career_lines = m.career | split: "|" %}
      {% for line in career_lines %}
      {% if line != "" %}<li>{{ line }}</li>{% endif %}
      {% endfor %}
    </ul>
    {% endif %}
    
    {% if m.advisory %}
    <p><strong>Industry Advisory:</strong> {{ m.advisory }}</p>
    {% endif %}
  </div>
</div>
{% endfor %}

---
{% endif %}

{% if phd.size > 0 %}
## Ph.D. Students

<div class="row row-cols-2 row-cols-md-4 g-4 mt-3">
{% for m in phd %}
  <div class="col text-center mb-4">
    <img class="img-fluid rounded mb-2" src="/assets/img/members/{{ m.photo }}" alt="{{ m.name_en }}" style="width:100px;height:100px;object-fit:cover;object-position:top;">
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
    <img class="img-fluid rounded mb-2" src="/assets/img/members/{{ m.photo }}" alt="{{ m.name_en }}" style="width:100px;height:100px;object-fit:cover;object-position:top;">
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
    <img class="img-fluid rounded mb-2" src="/assets/img/members/{{ m.photo }}" alt="{{ m.name_en }}" style="width:100px;height:100px;object-fit:cover;object-position:top;">
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
    <img class="img-fluid rounded mb-2" src="/assets/img/members/{{ m.photo }}" alt="{{ m.name_en }}" style="width:100px;height:100px;object-fit:cover;object-position:top;">
    <h5>{{ m.name_en }}</h5>
    <p>{{ m.graduation_info }}</p>
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

<div class="row row-cols-2 row-cols-md-4 g-4 mt-3">
  <div class="col text-center mb-4">
    <img class="img-fluid rounded mb-2" src="/assets/img/members/park_jaehyung.jpg" alt="Junhoe Park" style="width:100px;height:100px;object-fit:cover;object-position:top;">
    <h5>Junhoe Park</h5>
    <p>IT/AI</p>
  </div>
  <div class="col text-center mb-4">
    <img class="img-fluid rounded mb-2" src="/assets/img/members/baek_junha.png" alt="Junha Baek" style="width:100px;height:100px;object-fit:cover;object-position:top;">
    <h5>Junha Baek</h5>
    <p>Generative AI</p>
  </div>
  <div class="col text-center mb-4">
    <img class="img-fluid rounded mb-2" src="/assets/img/members/kim_gaon.jpg" alt="Gaon Kim" style="width:100px;height:100px;object-fit:cover;object-position:top;">
    <h5>Gaon Kim</h5>
    <p>Financial AI</p>
  </div>
  <div class="col text-center mb-4">
    <img class="img-fluid rounded mb-2" src="/assets/img/members/yoo_youngjun.png" alt="Youngjun Yu" style="width:100px;height:100px;object-fit:cover;object-position:top;">
    <h5>Youngjun Yu</h5>
    <p>IT/AI</p>
  </div>
  <div class="col text-center mb-4">
    <img class="img-fluid rounded mb-2" src="/assets/img/members/ahn_taehyun.png" alt="Taehyun Ahn" style="width:100px;height:100px;object-fit:cover;object-position:top;">
    <h5>Taehyun Ahn</h5>
    <p>AI Agent</p>
  </div>
  <div class="col text-center mb-4">
    <img class="img-fluid rounded mb-2" src="/assets/img/members/kim_seohyun.png" alt="Seohyun Kim" style="width:100px;height:100px;object-fit:cover;object-position:top;">
    <h5>Seohyun Kim</h5>
    <p>Healthcare AI</p>
  </div>
  <div class="col text-center mb-4">
    <img class="img-fluid rounded mb-2" src="/assets/img/members/lee_suhyeon.png" alt="Suhyeon Lee" style="width:100px;height:100px;object-fit:cover;object-position:top;">
    <h5>Suhyeon Lee</h5>
    <p>LLM</p>
  </div>
</div>

---

## M.S. Students

<div class="row row-cols-2 row-cols-md-4 g-4 mt-3">
  <div class="col text-center mb-4">
    <img class="img-fluid rounded mb-2" src="/assets/img/members/park_woohyun.png" alt="Woohyun Park" style="width:100px;height:100px;object-fit:cover;object-position:top;">
    <h5>Woohyun Park</h5>
    <p>Platform</p>
  </div>
</div>

---

## Undergraduate Researcher

<div class="row row-cols-2 row-cols-md-4 g-4 mt-3">
  <div class="col text-center mb-4">
    <img class="img-fluid rounded mb-2" src="/assets/img/members/seo_yeonwoo.jpg" alt="Yeonwoo Seo" style="width:100px;height:100px;object-fit:cover;object-position:top;">
    <h5>Yeonwoo Seo</h5>
    <p>Causal ML</p>
  </div>
</div>

---

## Alumni

<div class="row row-cols-2 row-cols-md-4 g-4 mt-3">
  <div class="col text-center mb-4">
    <img class="img-fluid rounded mb-2" src="/assets/img/members/yoo_woojeong.png" alt="Woojeong Yoo" style="width:100px;height:100px;object-fit:cover;object-position:top;">
    <h5>Woojeong Yoo</h5>
    <p>M.S. 2025 · PwC</p>
  </div>
</div>

{% endif %}
