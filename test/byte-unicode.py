#!/usr/bin/env python
# coding: utf-8

TEST = "byte-unicode"
execfile("head.inc")

tproc.set('UNICODEVAR', u'café')

execfile("foot.inc")
