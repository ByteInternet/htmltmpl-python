#!/usr/bin/env python

TEST = "nestcond"
execfile("head.inc")

#######################################################

tproc.set("title", "Template world.")
tproc.set("greeting", "Hello !")

tproc.set("var1", 1)
tproc.set("var2", 0)
tproc.set("var3", 1)

tproc.set("var4", 0)
tproc.set("var5", 0)

tproc.set("var6", 0)
tproc.set("var7", 1)

tproc.set("var8", 1)
tproc.set("var9", 0)

#######################################################

execfile("foot.inc")
