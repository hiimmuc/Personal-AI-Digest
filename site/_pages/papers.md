---
layout: modern
title: "All Papers"
permalink: /papers/
---

<div class="listing-header">
  <h1 class="listing-title">
    <span class="listing-icon" aria-hidden="true">📄</span>
    Research Papers
  </h1>
  <p class="listing-subtitle">Daily ArXiv papers curated &amp; summarized by AI</p>
  {% assign paper_posts = site.posts | where: "has_papers", true %}
  <div class="listing-stats">
    <span class="stat-pill">
      <strong>{{ paper_posts | size }}</strong> {% if paper_posts.size == 1 %}digest{% else %}digests{% endif %}
    </span>
  </div>
</div>

<div class="listing-grid">
{% assign paper_posts = site.posts | where: "has_papers", true %}
{% for post in paper_posts %}
<div class="listing-card listing-card--papers">
  <div class="listing-card-date">
    <span class="lc-day">{{ post.date | date: "%-d" }}</span>
    <span class="lc-mon">{{ post.date | date: "%b %Y" }}</span>
  </div>
  <div class="listing-card-body">
    {% if post.theme and post.theme != "" %}
    <p class="listing-card-theme">{{ post.theme }}</p>
    {% endif %}
    <div class="listing-card-meta">
      {% if post.paper_count %}
      <span class="lc-badge lc-badge--papers">
        <svg viewBox="0 0 16 16" fill="currentColor" width="12" height="12" aria-hidden="true"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 8.75 4.25V1.5Zm6.75.56v2.19c0 .138.112.25.25.25h2.19Z"/></svg>
        {{ post.paper_count }} {% if post.paper_count == 1 %}paper{% else %}papers{% endif %}
      </span>
      {% endif %}
      <span class="lc-badge lc-badge--date">{{ post.date | date: "%A, %b %-d" }}</span>
    </div>
    <div class="listing-card-actions">
      <a class="lc-btn lc-btn--primary" href="{{ post.url | relative_url }}#{{ post.papers_anchor | default: 'global-trends' }}">
        View Papers &rarr;
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
  <p>No research paper digests found yet.</p>
</div>
{% endfor %}
</div>
