---
layout: page
title: A Quant Blog
tagline: 
---
{% include JB/setup %}

Hi, I am Eric from Shanghai. Currently I work in a prop-trading house as an algo developer.
My interests lays on trend-following and stat-arb strategies, on either Chinese or foreign markets.
The main tool I use is Python.
Please leave a message or drop an email if you have any ideas to tell me.

<ul class="posts">
  {% for post in site.posts %}
    <li><span>{{ post.date | date_to_string }}</span> &raquo; <a href="{{ BASE_PATH }}{{ post.url }}">{{ post.title }}</a></li>
  {% endfor %}
</ul>
