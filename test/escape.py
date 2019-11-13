#!/usr/bin/env python

TEST = "escape"
exec(compile(open("head.inc", "rb").read(), "head.inc", 'exec'))

#######################################################

tproc.set("title", "Template world.")
tproc.set("greeting", "Hello !")
tproc.set("data", '<TAG PARAM="foo"> &entita; </TAG>')

#######################################################

exec(compile(open("foot.inc", "rb").read(), "foot.inc", 'exec'))
