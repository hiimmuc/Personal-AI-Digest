---
layout: modern
title: "Archive"
permalink: /archive/
---

# Archive

{% assign posts_by_month = site.posts | group_by_exp: "post", "post.date | date: '%B %Y'" %}

{% for month in posts_by_month %}

## {{ month.name }}

{% for post in month.items %}

- [{{ post.date | date: "%d %b" }} — Daily Digest]({{ post.url | relative_url }})
  ({{ post.content | split: "### " | size | minus: 1 }} sections)
{% endfor %}

{% assign weekly_posts = site.weekly | where_exp: "item", "item.date contains month.name" %}
{% for w in weekly_posts %}

- [{{ w.title }}]({{ w.url | relative_url }})
{% endfor %}

{% endfor %}
