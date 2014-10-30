#!/usr/bin/env python

import time

TEST = "multipart"
execfile("head.inc")

#######################################################

tproc.set("title", "Template world.")
tproc.set("greeting", "Hello !")

output = tproc.process(template, 1)
# time.sleep(1)

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

output += tproc.process(template, 2)
# time.sleep(1)

#######################################################

execfile("foot.inc")
