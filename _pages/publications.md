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

<h2>Journals</h2>

{% bibliography --query @article* %}

<div style="margin-top: 3rem;"></div>

<h2>Conferences</h2>

{% bibliography --query @inproceedings* %}

</div>
