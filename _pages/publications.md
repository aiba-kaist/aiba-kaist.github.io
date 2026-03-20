---
layout: page
permalink: /publications/
title: publications
description: Publications from AIBA Lab in reversed chronological order.
nav: true
nav_order: 3
---

<!-- _pages/publications.md -->

<!-- Author Filter Banner -->
<div id="authorFilter" style="display:none; background:#e7f5ff; padding:12px 16px; border-radius:8px; margin-bottom:20px;">
  <span>Showing publications by: <strong id="authorName"></strong></span>
  <button onclick="clearFilter()" style="margin-left:12px; padding:4px 12px; border:1px solid #228be6; background:white; border-radius:4px; cursor:pointer;">Show All</button>
</div>

<!-- Bibsearch Feature -->

{% include bib_search.liquid %}

<div class="publications">

<h2>Journals</h2>

{% bibliography --query @article* %}

<div style="margin-top: 3rem;"></div>

<h2>Conferences</h2>

{% bibliography --query @inproceedings* %}

</div>

<script>
function filterByAuthor() {
  const params = new URLSearchParams(window.location.search);
  const author = params.get('author');
  if (!author) return;
  
  document.getElementById('authorFilter').style.display = 'block';
  document.getElementById('authorName').textContent = author;
  
  document.querySelectorAll('.bibliography li').forEach(li => {
    const authorText = li.querySelector('.author')?.textContent?.toLowerCase() || '';
    if (!authorText.includes(author.toLowerCase())) {
      li.style.display = 'none';
    }
  });
}

function clearFilter() {
  window.location.href = '/publications/';
}

document.addEventListener('DOMContentLoaded', filterByAuthor);
</script>
