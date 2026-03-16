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

<h2 style="margin-top: 2rem; margin-bottom: 1.5rem;">Journal Articles</h2>

{% bibliography --query @article* %}

<div style="margin-top: 3rem;"></div>

<h2 style="margin-top: 2rem; margin-bottom: 1.5rem;">Conference Papers</h2>

{% bibliography --query @inproceedings* %}

</div>
