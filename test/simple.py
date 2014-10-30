#!/usr/bin/env python

TEST = "simple"
execfile("head.inc")

#######################################################

tproc.set("title", "Template world.")
tproc.set("greeting", "Hello !")

#######################################################

execfile("foot.inc")
