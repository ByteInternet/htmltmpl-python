#!/usr/bin/env python

TEST = "byte-case-insensitive"
exec(compile(open("head.inc", "rb").read(), "head.inc", 'exec'))

tproc.set('UVAR', 'yes')
tproc.set('ULOOPVAR', [{'VAR': 'yes'}])

tproc.set('lvar', 'yes')
tproc.set('lloopvar', [{'var': 'yes'}])

exec(compile(open("foot.inc", "rb").read(), "foot.inc", 'exec'))
