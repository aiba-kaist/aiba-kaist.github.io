---
layout: page
title: news
permalink: /news/
nav: true
nav_order: 4
---

{% assign news_items = site.data.admin_data.news | sort: 'date' | reverse %}
{% if news_items and news_items.size > 0 %}
{% assign grouped = news_items | group_by_exp: 'item', "item.date | date: '%Y'" %}

<div class="news-page">
  {% for yg in grouped %}
    <h2 class="news-year mt-4">{{ yg.name }}</h2>
    <ul class="news-list" style="list-style: none; padding-left: 0;">
      {% for item in yg.items %}
        <li class="mb-3">
          <span class="news-date" style="font-weight: 600;">[{{ item.date | date: '%b %d' }}]</span>
          {{ item.content | emojify }}
        </li>
      {% endfor %}
    </ul>
  {% endfor %}
</div>
{% else %}

<p>No news so far...</p>
{% endif %}
