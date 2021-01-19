#!/usr/bin/env python

TEST = "globalvars"
exec(compile(open("head.inc", "rb").read(), "head.inc", 'exec'))

#######################################################

tproc.set("title", "Template world.")
tproc.set("greeting", "Hello !")
tproc.set("Loop1", [ {} ])

#######################################################

exec(compile(open("foot.inc", "rb").read(), "foot.inc", 'exec'))
