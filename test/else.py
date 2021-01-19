#!/usr/bin/env python

TEST = "else"
exec(compile(open("head.inc", "rb").read(), "head.inc", 'exec'))

#######################################################

tproc.set("title", "Stranka")
tproc.set("true", 1)
tproc.set("false", 0)

#######################################################

exec(compile(open("foot.inc", "rb").read(), "foot.inc", 'exec'))

