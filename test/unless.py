#!/usr/bin/env python

TEST = "unless"
exec(compile(open("head.inc", "rb").read(), "head.inc", 'exec'))

#######################################################

tproc.set("true", 1)
tproc.set("false", 0)
tproc.set("true2", 1)

#######################################################

exec(compile(open("foot.inc", "rb").read(), "foot.inc", 'exec'))
