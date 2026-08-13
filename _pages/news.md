---
layout: page
title: news
permalink: /news/
nav: true
nav_order: 1
---

<style>
  .news-page .news-year {
    display: flex;
    align-items: center;
    gap: 1rem;
    font-size: 1.6rem;
    font-weight: 700;
    margin: 2.6rem 0 1.4rem;
  }
  .news-page .news-year:first-child {
    margin-top: 0.5rem;
  }
  .news-page .news-year::after {
    content: "";
    flex: 1;
    height: 1px;
    background: var(--global-divider-color);
  }
  .news-page .news-item {
    display: flex;
    align-items: baseline;
    gap: 1rem;
    margin-bottom: 1rem;
  }
  .news-page .news-badge {
    flex: none;
    width: 3.6rem;
    text-align: center;
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.04em;
    text-transform: uppercase;
    white-space: nowrap;
    color: var(--global-theme-color);
    border: 1px solid var(--global-theme-color);
    border-radius: 999px;
    padding: 0.18rem 0.55rem;
  }
  .news-page .news-text {
    flex: 1;
    line-height: 1.65;
  }
</style>

{% assign news_items = site.data.admin_data.news | sort: 'date' | reverse %}
{% if news_items and news_items.size > 0 %}
{% assign grouped = news_items | group_by_exp: 'item', "item.date | date: '%Y'" %}

<div class="news-page">
  {% for yg in grouped %}
    <h2 class="news-year">{{ yg.name }}</h2>
    {% for item in yg.items %}
      <div class="news-item">
        <span class="news-badge">{{ item.date | date: '%b' }}</span>
        <div class="news-text">{{ item.content | markdownify | remove: '<p>' | remove: '</p>' | emojify }}</div>
      </div>
    {% endfor %}
  {% endfor %}
</div>
{% else %}

<p>No news so far...</p>
{% endif %}
