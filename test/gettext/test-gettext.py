#!/usr/bin/env python

import sys
import gettext
import locale
sys.path.insert(0, "../..")
from htmltmpl import TemplateManager, TemplateProcessor

locale.setlocale(locale.LC_MESSAGES, "en_US")
gettext.bindtextdomain("test", "./locale")
gettext.textdomain("test")

man = TemplateManager(precompile = 0, gettext = 1, debug = 1)
tmpl = man.prepare("gettext.tmpl")
tproc = TemplateProcessor(debug = 1)
tproc.set("title", "Gettext test page")
print tproc.process(tmpl)

