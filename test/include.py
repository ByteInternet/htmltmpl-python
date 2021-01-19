#!/usr/bin/env python

TEST = "include"
exec(compile(open("head.inc", "rb").read(), "head.inc", 'exec'))

#######################################################

tproc.set("title", "Template world.")
tproc.set("greeting", "Hello !")

#######################################################

exec(compile(open("foot.inc", "rb").read(), "foot.inc", 'exec'))
