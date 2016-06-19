#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Tianfu He'
SITENAME = u'Tianfu.D.He'
SITEURL = 'http://tianfudhe.github.io'

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
SOCIAL = (('EMail', 'mailto:Tianfu.D.He@outlook.com'),
          ('Github', 'https://github.com/tianfudhe'),)

DEFAULT_PAGINATION = 8

########################### Added by me

PLUGIN_PATHS = ["./plugins"]
PLUGINS = ["render_math"]

THEME = "pelican-themes/alchemy"

DISQUS_SITENAME = u'tianfudhe'

EMAIL_ADDRESS = "tianfu.d.he@gmail.com"
GITHUB_ADDRESS = "https://github.com/tianfudhe"
TWITTER_ADDRESS = "https://twitter.com/HeTianfu"
PROFILE_IMAGE="images/me.png"
MENU_ITEMS = (("About 何天赋", "welcome-to-my-blog.html"),)
CATEGORIES_ON_MENU = True
TAGS_ON_MENU = True

############################
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
