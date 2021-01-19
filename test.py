#!/usr/bin/env python

import os
import sys
import re

os.chdir("test")

# If this is not a UNIX platform, then
# we must convert the .tmpl and .res files to make it compatible
# with newline separator used on current platform.
if os.linesep != "\n":
    print("This is not UNIX.")
    print("Converting newline separators in .tmpl and .res files.")
    files = [x for x in os.listdir(".") \
               if x.find(".tmpl") != -1 or x.find(".res") != -1]
    files.sort()
    for file in files:
        old = open(file).read()
        new = re.sub("\n", os.linesep, old)
        open(file, "w").write(new)

# Exec all .py files located in the "test" directory.
scripts = [x for x in os.listdir(".") if x.find(".py") != -1]
scripts.sort()

for i in range(len(scripts)):
    print(i+1, "...", end=' ')
    exec(compile(open(scripts[i], "rb").read(), scripts[i], 'exec'))
