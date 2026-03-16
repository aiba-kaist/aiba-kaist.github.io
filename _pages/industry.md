---
layout: page
permalink: /industry/
title: industry
description: Our industry partners and collaborations
nav: true
nav_order: 4
---

{% assign industry_data = site.data.admin_data.industry %}

{% if industry_data %}

{% assign collaborators = industry_data | where: "type", "Collaborator" %}
{% assign funding = industry_data | where: "type", "Funding" %}

## Collaborators

<div class="row row-cols-3 row-cols-md-4 g-4 mt-3">
{% for p in collaborators %}
  <div class="col text-center mb-3">
    <img class="img-fluid" src="/assets/img/partners/{{ p.logo }}" alt="{{ p.name }}" style="max-height:56px;object-fit:contain;">
  </div>
{% endfor %}
</div>

---

## Funding

<div class="row row-cols-3 row-cols-md-4 g-4 mt-3">
{% for p in funding %}
  <div class="col text-center mb-3">
    <img class="img-fluid" src="/assets/img/partners/{{ p.logo }}" alt="{{ p.name }}" style="max-height:56px;object-fit:contain;">
  </div>
{% endfor %}
</div>

{% else %}

<!-- Fallback: 기존 하드코딩 데이터 -->

## Collaborators

<div class="row row-cols-3 row-cols-md-4 g-4 mt-3">
  <div class="col text-center mb-3">
    <img class="img-fluid" src="/assets/img/partners/baemin.jpg" alt="Baemin" style="max-height:56px;object-fit:contain;">
  </div>
  <div class="col text-center mb-3">
    <img class="img-fluid" src="/assets/img/partners/hankook.png" alt="Hankook Tire" style="max-height:56px;object-fit:contain;">
  </div>
  <div class="col text-center mb-3">
    <img class="img-fluid" src="/assets/img/partners/htbeyond.png" alt="HTbeyond" style="max-height:56px;object-fit:contain;">
  </div>
  <div class="col text-center mb-3">
    <img class="img-fluid" src="/assets/img/partners/classu.png" alt="ClassU" style="max-height:56px;object-fit:contain;">
  </div>
  <div class="col text-center mb-3">
    <img class="img-fluid" src="/assets/img/partners/ssb.png" alt="Social Solidarity Bank" style="max-height:56px;object-fit:contain;">
  </div>
  <div class="col text-center mb-3">
    <img class="img-fluid" src="/assets/img/partners/qanda.jpg" alt="QANDA" style="max-height:56px;object-fit:contain;">
  </div>
</div>

---

## Funding

<div class="row row-cols-3 row-cols-md-4 g-4 mt-3">
  <div class="col text-center mb-3">
    <img class="img-fluid" src="/assets/img/partners/nrf.png" alt="NRF" style="max-height:56px;object-fit:contain;">
  </div>
  <div class="col text-center mb-3">
    <img class="img-fluid" src="/assets/img/partners/iitp.jpg" alt="IITP" style="max-height:56px;object-fit:contain;">
  </div>
</div>

{% endif %}
