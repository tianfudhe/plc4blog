Title: How-To Render Math in Pelican
Date: 2016-05-13 13:17
Category: How-To's
Tags: ubuntu

# Render Math in Pelican
When you get your research notes done with latex syntax in `.md`, and prepared to generate the site and `git push` it to your Github Page, terrible things happend that **Latex syntax parts are not rendered with Mathjax!**.  
This article introduces a convenient configure to your Pelican that once done, pages with Mathjax are generated **without** extra work.

## Install Pelican Plugin `render-math`
To render Latex math, we need to install the Pelican plugin `render-math`.
The source of `render-math` and installation instruction is provided [here](https://github.com/getpelican/pelican-plugins.git).
BTW, to my experience, you can simply integrate `render-math` in your Pelican project.

## A Bit More Dirty Work
Even `render-math` is installed, not a few would still suffer from the rendering. This can be caused by the python package `markdown` which does not support Mathjax. Thanks to the solution provided in [this page](http://wittawat.com/pelican_mathjax.html), we need to enhance the `markdown` python package with math rendering, the detailed instruction is [here](https://github.com/mayoff/python-markdown-mathjax).