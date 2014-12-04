#!/usr/bin/env python

TEST = "byte"
execfile("head.inc")

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

execfile("foot.inc")
