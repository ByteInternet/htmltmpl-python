#!/usr/bin/env python
# coding: utf-8

TEST = "byte-unicode"
exec(compile(open("head.inc", "rb").read(), "head.inc", 'exec'))

tproc.set('UNICODEVAR', 'café')

exec(compile(open("foot.inc", "rb").read(), "foot.inc", 'exec'))
