#!/usr/bin/env python

TEST = "byte"
exec(compile(open("head.inc", "rb").read(), "head.inc", 'exec'))

#######################################################

tproc.set("DOMAIN", "example.com")

files = [
    {'FILE': 'file 1'},
    {'FILE': 'file 2'},
    ]

incompatible_files = [
    {'FILE': 'incompatible file 1'},
    {'FILE': 'incompatible file 2'},
    ]

tproc.set('ALL', files)
tproc.set('INCOMPATIBLE', incompatible_files)


#######################################################

exec(compile(open("foot.inc", "rb").read(), "foot.inc", 'exec'))
