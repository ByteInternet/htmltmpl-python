#!/usr/bin/env python

TEST = "include"
execfile("head.inc")

#######################################################

tproc.set("title", "Template world.")
tproc.set("greeting", "Hello !")

#######################################################

execfile("foot.inc")
