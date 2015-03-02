#!/usr/bin/env python

TEST = "byte-case-insensitive"
execfile("head.inc")

tproc.set('UVAR', 'yes')
tproc.set('ULOOPVAR', [{'VAR': 'yes'}])

tproc.set('lvar', 'yes')
tproc.set('lloopvar', [{'var': 'yes'}])

execfile("foot.inc")
