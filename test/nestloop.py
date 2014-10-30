#!/usr/bin/env python

TEST = "nestloop"
execfile("head.inc")

#######################################################

tproc.set("title", "Template world.")
tproc.set("greeting", "Hello !")
tproc.set("Loop1", [
    { "Loop2" : [ {}, {} ], 
      "Loop3" : [], 
      "Loop4" : [ { "Loop6" : [
        {}, {}, {}
      ] } ], 
      "Loop5" : [] },

    { "Loop2" : [], 
      "Loop3" : [ {}, {} ], 
      "Loop4" : [], 
      "Loop5" : [ {} ] }
])

#######################################################

execfile("foot.inc")
