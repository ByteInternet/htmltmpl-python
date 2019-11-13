#!/usr/bin/env python

TEST = "compiled"

import sys
import os
sys.path.insert(0, "..")

from htmltmpl import TemplateManager, TemplateProcessor

man = TemplateManager(precompile = 1, debug = "debug" in sys.argv)
template = man.prepare(TEST + ".tmpl")
tproc = TemplateProcessor(debug = "debug" in sys.argv)

#######################################################

def fill(tproc):
    tproc.set("title", "Template world.")
    tproc.set("greeting", "Hello !")
    tproc.set("Boys", [
        { "name" : "Tomas",  "age" : 19 },
        { "name" : "Pavel",  "age" : 34 },
        { "name" : "Janek",  "age" : 67 },
        { "name" : "Martin", "age" : 43 },
        { "name" : "Viktor", "age" : 78 },
        { "name" : "Marian", "age" : 90 },
        { "name" : "Prokop", "age" : 23 },
        { "name" : "Honzik", "age" : 46 },
        { "name" : "Brudra", "age" : 64 },
        { "name" : "Marek",  "age" : 54 },
        { "name" : "Peter",  "age" : 42 },
        { "name" : "Beda",   "age" : 87 }
    ])

#######################################################

fill(tproc)
tproc.process(template)
tproc.reset()

fill(tproc)
tproc.process(template)
tproc.reset()

fill(tproc)
output = tproc.process(template)

if "out" in sys.argv:
    sys.stdout.write(output)
    sys.exit(0)

res = open("%s.res" % TEST).read()

print(TEST, "...", end=' ')

if output == res and os.access("%s.tmplc" % TEST, os.R_OK):
    print("OK")
    os.remove("%s.tmplc" % TEST)
else:
    print("FAILED")
    open("%s.fail" % TEST, "w").write(output)
