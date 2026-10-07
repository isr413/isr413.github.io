---
title: Table of Contents
description: A map of everything on this site, kept up to date automatically.
pinned: true
---

This page lists everything on the site. It updates itself whenever a post, app, or deck is added.

## About me

- [Home]({{ '/' | relative_url }}): who I am, what I teach, and how to reach me
- [Faculty page]({{ site.person.faculty_url }}) at the {{ site.person.organization }}
- [Add me to your contacts]({{ '/contact.vcf' | relative_url }}) (vCard)
- [Printable QR code]({{ '/qr.html' | relative_url }}) for sharing this site

## Blog posts
{% assign others = site.posts | where_exp: "p", "p.pinned != true" %}
{% if others.size > 0 %}
<ul>
{%- for post in others %}
  <li><a href="{{ post.url | relative_url }}">{{ post.title }}</a> <span class="muted">({{ post.date | date: "%B %-d, %Y" }})</span></li>
{%- endfor %}
</ul>
{% else %}
No posts yet. New posts will appear here and on the [Blog]({{ '/blog/' | relative_url }}) page.
{% endif %}

## Interactive apps

<ul>
{%- for app in site.data.apps %}
  <li><a href="{{ app.url | relative_url }}">{{ app.title }}</a>: {{ app.description }}</li>
{%- endfor %}
</ul>

See all of them on the [Apps]({{ '/apps/' | relative_url }}) page.

## Slide decks

{% include deck-groups.html style="list" %}

See all of them on the [Decks]({{ '/decks/' | relative_url }}) page.
