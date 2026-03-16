---
layout: page
permalink: /publications/
title: publications
description: Publications from AIBA Lab in reversed chronological order.
nav: true
nav_order: 3
---

<!-- _pages/publications.md -->

<!-- Bibsearch Feature -->

{% include bib_search.liquid %}

<div class="publications">

## Journal Articles

{% bibliography --query @article* %}

<div class="my-5"></div>

## Conference Papers

{% bibliography --query @inproceedings* %}

</div>
