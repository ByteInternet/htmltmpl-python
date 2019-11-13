#!/usr/bin/env python

TEST = "params"
exec(compile(open("head.inc", "rb").read(), "head.inc", 'exec'))

#######################################################

tproc.set("title", "Template world.")
tproc.set("greeting", "Hello <HTML> world !")
tproc.set("Loop", [ {} ])

#######################################################

exec(compile(open("foot.inc", "rb").read(), "foot.inc", 'exec'))
