#!/usr/bin/env python

TEST = "nestloop"
exec(compile(open("head.inc", "rb").read(), "head.inc", 'exec'))

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

exec(compile(open("foot.inc", "rb").read(), "foot.inc", 'exec'))
