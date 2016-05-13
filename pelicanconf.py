#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Tianfu He'
SITENAME = u'Tianfu.D.He'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('EMail', 'mailto:tianfu.d.he@gmail.com'),
          ('Github', 'https://github.com/tianfudhe'),)

DEFAULT_PAGINATION = 8



################ Added by me
PLUGIN_PATHS = ["./plugins"]
PLUGINS = ["render_math", u"disqus_static"]

THEME = "notmyidea"

DISQUS_SITENAME = 'tianfudhe'
DISQUS_SECRET_KEY = u'OExuIWfqKsotjYYOzpXF7ES5f8PlvYhler5vvdWOPt9QyAixkkCpmvsVzqgJZrO6'
DISQUS_PUBLIC_KEY = u'hr6h4Sq5yoWQmf7yJUDfdVMKXkJMkEt97VKQBNEn8VP9drMv93F4m4gLgsBwcxpZ'

############################


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
