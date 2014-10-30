#!/usr/bin/env python

TEST = "globalvars"
execfile("head.inc")

#######################################################

tproc.set("title", "Template world.")
tproc.set("greeting", "Hello !")
tproc.set("Loop1", [ {} ])

#######################################################

execfile("foot.inc")
