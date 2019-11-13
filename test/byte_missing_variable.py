#!/usr/bin/env python

TEST = "byte_missing_variable"
exec(compile(open("head.inc", "rb").read(), "head.inc", 'exec'))

#######################################################


#######################################################

exec(compile(open("foot.inc", "rb").read(), "foot.inc", 'exec'))
