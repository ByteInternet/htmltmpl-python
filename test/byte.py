#!/usr/bin/env python

TEST = "byte"
execfile("head.inc")

#######################################################

tproc.set("domain", "example.com")  # < Must be lower-case

files = [
    {'file': 'file 1'},
    {'file': 'file 2'},
    ]

incompatible_files = [
    {'file': 'incompatible file 1'},
    {'file': 'incompatible file 2'},
    ]

tproc.set('All', files)  # < Must be Capitalized
tproc.set('incompatible', 1)  # < Must be lowercase (boolean)
tproc.set('Incompatible', incompatible_files)  # < Must be Capitalized


#######################################################

execfile("foot.inc")
