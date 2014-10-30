#!/usr/bin/env python

TEST = "unless"
execfile("head.inc")

#######################################################

tproc.set("true", 1)
tproc.set("false", 0)
tproc.set("true2", 1)

#######################################################

execfile("foot.inc")
