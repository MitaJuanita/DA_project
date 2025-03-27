---
layout: default
title: Healthcare Data & Interface Blog
description: Technical insights on healthcare integration and data analytics
---

# Healthcare Integration Blog

Welcome to my technical blog where I share insights about:
- HL7/FHIR integration challenges
- Healthcare data analytics
- System interoperability solutions
- Best practices and lessons learned
- AI usese for interoperability and Data Analytics

## Recent Posts
{% for post in site.posts limit:5 %}
* [{{ post.title }}]({{ post.url | relative_url }}) - {{ post.date | date: "%B %d, %Y" }}
{% endfor %}