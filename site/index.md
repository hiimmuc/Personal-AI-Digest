---
layout: modern
title: "AI Digest"
permalink: /
---

{% assign all_posts = site.posts %}
{% if all_posts.size > 0 %}

{% assign today_post = all_posts | first %}

<!-- ── Today's featured digest ─────────────────────────────── -->
<article class="home-featured" aria-label="Today's digest">
  <div class="hf-header">
    <div class="hf-label">
      <span class="hf-dot" aria-hidden="true"></span>
      Today
    </div>
    <time class="hf-date" datetime="{{ today_post.date | date: '%Y-%m-%d' }}">
      {{ today_post.date | date: "%A, %B %-d, %Y" }}
    </time>
  </div>

  {% if today_post.summary and today_post.summary != "" %}
  <div class="hf-summary">
    {{ today_post.summary | markdownify }}
  </div>
  {% elsif today_post.theme and today_post.theme != "" %}
  <p class="hf-theme">{{ today_post.theme }}</p>
  {% endif %}

  <div class="hf-stats">
    {% if today_post.paper_count and today_post.paper_count > 0 %}
    <span class="hf-stat hf-stat--papers">
      <svg viewBox="0 0 16 16" fill="currentColor" width="13" height="13" aria-hidden="true"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 8.75 4.25V1.5Zm6.75.56v2.19c0 .138.112.25.25.25h2.19Z"/></svg>
      {{ today_post.paper_count }} {% if today_post.paper_count == 1 %}paper{% else %}papers{% endif %}
    </span>
    {% endif %}
    {% if today_post.news_count and today_post.news_count > 0 %}
    <span class="hf-stat hf-stat--news">
      <svg viewBox="0 0 16 16" fill="currentColor" width="13" height="13" aria-hidden="true"><path d="M0 2.75C0 1.784.784 1 1.75 1h12.5c.966 0 1.75.784 1.75 1.75v8.5A1.75 1.75 0 0 1 14.25 13H1.75A1.75 1.75 0 0 1 0 11.25ZM1.75 2.5a.25.25 0 0 0-.25.25v8.5c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25v-8.5a.25.25 0 0 0-.25-.25Z"/><path d="M5 8.5h6a.75.75 0 0 1 0 1.5H5a.75.75 0 0 1 0-1.5Zm0-3h6a.75.75 0 0 1 0 1.5H5A.75.75 0 0 1 5 5.5Z"/></svg>
      {{ today_post.news_count }} {% if today_post.news_count == 1 %}item{% else %}items{% endif %}
    </span>
    {% endif %}
    {% if today_post.github_trending_count and today_post.github_trending_count > 0 %}
    <span class="hf-stat hf-stat--trending">
      <svg viewBox="0 0 16 16" fill="currentColor" width="13" height="13" aria-hidden="true"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
      {{ today_post.github_trending_count }} trending {% if today_post.github_trending_count == 1 %}repo{% else %}repos{% endif %}
    </span>
    {% endif %}
  </div>

  <div class="hf-actions">
    {% if today_post.has_papers %}
    <a class="hf-btn hf-btn--papers" href="{{ today_post.url | relative_url }}#{{ today_post.papers_anchor | default: 'global-trends' }}">
      📄 Research Papers
    </a>
    {% endif %}
    {% if today_post.has_news %}
    <a class="hf-btn hf-btn--news" href="{{ today_post.url | relative_url }}#tech-news">
      📰 Tech News
    </a>
    {% endif %}
    {% if today_post.has_github_trending %}
    <a class="hf-btn hf-btn--trending" href="{{ today_post.url | relative_url }}#github-trending">
      🔥 Trending
    </a>
    {% endif %}
    <a class="hf-btn hf-btn--ghost" href="{{ today_post.url | relative_url }}">
      Full Digest →
    </a>
  </div>
</article>

<!-- ── Previous digests ────────────────────────────────────── -->
{% assign older_posts = all_posts | slice: 1, 9 %}
{% if older_posts.size > 0 %}
<section class="home-previous" aria-label="Previous digests">
  <h2 class="prev-heading">Previous Digests</h2>
  <div class="prev-list">
    {% for post in older_posts %}
    <a class="prev-card" href="{{ post.url | relative_url }}">
      <div class="prev-card-date">
        <span class="prev-day">{{ post.date | date: "%-d" }}</span>
        <span class="prev-mon">{{ post.date | date: "%b" }}</span>
      </div>
      <div class="prev-card-body">
        <div class="prev-card-meta">
          {% if post.paper_count and post.paper_count > 0 %}
          <span class="prev-badge prev-badge--papers">{{ post.paper_count }}p</span>
          {% endif %}
          {% if post.news_count and post.news_count > 0 %}
          <span class="prev-badge prev-badge--news">{{ post.news_count }}n</span>
          {% endif %}
          {% if post.github_trending_count and post.github_trending_count > 0 %}
          <span class="prev-badge prev-badge--trending">{{ post.github_trending_count }}🔥</span>
          {% endif %}
        </div>
        {% if post.theme and post.theme != "" %}
        <p class="prev-card-theme">{{ post.theme | truncate: 100 }}</p>
        {% endif %}
      </div>
    </a>
    {% endfor %}
  </div>
</section>
{% endif %}

{% else %}
<div class="listing-empty">
  <span class="listing-empty-icon" aria-hidden="true">🚀</span>
  <p>No digests published yet. Check back soon!</p>
</div>
{% endif %}
