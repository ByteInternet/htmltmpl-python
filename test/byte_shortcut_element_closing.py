#!/usr/bin/env python

TEST = "byte_shortcut_element_closing"
exec(compile(open("head.inc", "rb").read(), "head.inc", 'exec'))

#######################################################

tproc.set("TEST", "HELLO WORLD")

#######################################################

exec(compile(open("foot.inc", "rb").read(), "foot.inc", 'exec'))
