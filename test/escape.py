#!/usr/bin/env python

TEST = "escape"
execfile("head.inc")

#######################################################

tproc.set("title", "Template world.")
tproc.set("greeting", "Hello !")
tproc.set("data", '<TAG PARAM="foo"> &entita; </TAG>')

#######################################################

execfile("foot.inc")
