
import sys
import os
sys.path.insert(0, "..")

from htmltmpl import TemplateManager, TemplateProcessor

man = TemplateManager(precompile = 0, debug = "debug" in sys.argv)
template = man.prepare(TEST + ".tmpl")
tproc = TemplateProcessor(debug = "debug" in sys.argv)
output = ""
