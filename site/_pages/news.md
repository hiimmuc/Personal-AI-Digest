---
layout: modern
title: "All News"
permalink: /news/
---

<div class="listing-header">
  <h1 class="listing-title">
    <span class="listing-icon" aria-hidden="true">📰</span>
    Tech News
  </h1>
  <p class="listing-subtitle">Daily tech &amp; AI news from Hacker News, Reddit ML, and more</p>
  {% assign news_posts = site.posts | where: "has_news", true %}
  <div class="listing-stats">
    <span class="stat-pill">
      <strong>{{ news_posts | size }}</strong> {% if news_posts.size == 1 %}digest{% else %}digests{% endif %}
    </span>
  </div>
</div>

<div class="listing-grid">
{% assign news_posts = site.posts | where: "has_news", true %}
{% for post in news_posts %}
<div class="listing-card listing-card--news">
  <div class="listing-card-date">
    <span class="lc-day">{{ post.date | date: "%-d" }}</span>
    <span class="lc-mon">{{ post.date | date: "%b %Y" }}</span>
  </div>
  <div class="listing-card-body">
    {% if post.theme and post.theme != "" %}
    <p class="listing-card-theme">{{ post.theme }}</p>
    {% endif %}
    <div class="listing-card-meta">
      {% if post.news_count %}
      <span class="lc-badge lc-badge--news">
        <svg viewBox="0 0 16 16" fill="currentColor" width="12" height="12" aria-hidden="true"><path d="M0 2.75C0 1.784.784 1 1.75 1h12.5c.966 0 1.75.784 1.75 1.75v8.5A1.75 1.75 0 0 1 14.25 13H1.75A1.75 1.75 0 0 1 0 11.25ZM1.75 2.5a.25.25 0 0 0-.25.25v8.5c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25v-8.5a.25.25 0 0 0-.25-.25Z"/><path d="M5 8.5h6a.75.75 0 0 1 0 1.5H5a.75.75 0 0 1 0-1.5Zm0-3h6a.75.75 0 0 1 0 1.5H5A.75.75 0 0 1 5 5.5Z"/></svg>
        {{ post.news_count }} {% if post.news_count == 1 %}item{% else %}items{% endif %}
      </span>
      {% endif %}
      <span class="lc-badge lc-badge--date">{{ post.date | date: "%A, %b %-d" }}</span>
    </div>
    <div class="listing-card-actions">
      <a class="lc-btn lc-btn--primary lc-btn--news" href="{{ post.url | relative_url }}#tech-news">
        Read News &rarr;
      </a>
      <a class="lc-btn lc-btn--ghost" href="{{ post.url | relative_url }}">
        Full Digest
      </a>
    </div>
  </div>
</div>
{% else %}
<div class="listing-empty">
  <span class="listing-empty-icon" aria-hidden="true">📭</span>
  <p>No news digests found yet.</p>
</div>
{% endfor %}
</div>
