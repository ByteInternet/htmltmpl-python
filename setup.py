#!/usr/bin/env python
import os

from setuptools import setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(name = "htmltmpl",
      version = "1.22",
      description = "Templating engine for separation of code and HTML.",
      author = "Tomas Styblo",
      author_email = "tripie@cpan.org",
      url = "http://htmltmpl.sourceforge.net/",
      licence = "GNU GPL",
      py_modules = ['htmltmpl', 'easydoc', 'easydocp']
     )
