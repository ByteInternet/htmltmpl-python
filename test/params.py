#!/usr/bin/env python

TEST = "params"
execfile("head.inc")

#######################################################

tproc.set("title", "Template world.")
tproc.set("greeting", "Hello <HTML> world !")
tproc.set("Loop", [ {} ])

#######################################################

execfile("foot.inc")
