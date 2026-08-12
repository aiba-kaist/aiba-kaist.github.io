---
layout: page
permalink: /gallery/
title: gallery
description: Photos and memories from AIBA Lab
nav: true
nav_order: 7
---

{% assign gallery_data = site.data.admin_data.gallery %}

{% if gallery_data %}

{% assign conferences = gallery_data | where: "category", "Conferences" %}
{% assign lab_life = gallery_data | where: "category", "Lab Life" %}

## Conferences & Events

<div class="row mt-3">
{% for p in conferences %}
  <div class="col-sm-6 col-md-4 mb-4">
    <img class="img-fluid rounded" src="/assets/img/gallery/{{ p.image }}" alt="{{ p.caption }}">
    <p class="text-center mt-2">{{ p.caption }}</p>
  </div>
{% endfor %}
</div>

<div class="my-5"></div>

---

<div class="my-4"></div>

## Lab Life

<div class="row mt-3">
{% for p in lab_life %}
  <div class="col-sm-6 col-md-4 mb-4">
    <img class="img-fluid rounded" src="/assets/img/gallery/{{ p.image }}" alt="{{ p.caption }}">
    <p class="text-center mt-2">{{ p.caption }}</p>
  </div>
{% endfor %}
</div>

{% else %}

<!-- Fallback: 기존 하드코딩 데이터 -->

## Conferences & Events

<div class="row mt-3">
  <div class="col-sm-6 col-md-4 mb-4">
    <img class="img-fluid rounded" src="/assets/img/gallery/cist.png" alt="CIST 2024">
    <p class="text-center mt-2">CIST 2024, Atlanta</p>
  </div>
  <div class="col-sm-6 col-md-4 mb-4">
    <img class="img-fluid rounded" src="/assets/img/gallery/wits.png" alt="WITS 2024">
    <p class="text-center mt-2">WITS 2024, Nashville</p>
  </div>
  <div class="col-sm-6 col-md-4 mb-4">
    <img class="img-fluid rounded" src="/assets/img/gallery/cikm.jpg" alt="CIKM 2025">
    <p class="text-center mt-2">CIKM 2025</p>
  </div>
  <div class="col-sm-6 col-md-4 mb-4">
    <img class="img-fluid rounded" src="/assets/img/gallery/joint-seminar.png" alt="Joint Lab Seminar">
    <p class="text-center mt-2">KAIST-UBC-ASU Joint Seminar</p>
  </div>
</div>

<div class="my-5"></div>

---

<div class="my-4"></div>

## Lab Life

<div class="row mt-3">
  <div class="col-sm-6 col-md-4 mb-4">
    <img class="img-fluid rounded" src="/assets/img/gallery/teachers-day.png" alt="Teachers Day">
    <p class="text-center mt-2">스승의 날 이벤트</p>
  </div>
  <div class="col-sm-6 col-md-4 mb-4">
    <img class="img-fluid rounded" src="/assets/img/gallery/year-end.png" alt="Year End Party">
    <p class="text-center mt-2">2025 송년회</p>
  </div>
  <div class="col-sm-6 col-md-4 mb-4">
    <img class="img-fluid rounded" src="/assets/img/gallery/lab-team.jpg" alt="Lab Team">
    <p class="text-center mt-2">Lab Team Photo</p>
  </div>
</div>

{% endif %}
