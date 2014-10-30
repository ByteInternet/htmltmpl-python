#!/usr/bin/env python

TEST = "maxinclude"
execfile("head.inc")

#######################################################

tproc.set("title", "Template world.")
tproc.set("greeting", "Hello !")

#######################################################

execfile("foot.inc")
