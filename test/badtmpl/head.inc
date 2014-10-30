
import sys
import os
from htmltmpl import TemplateManager, TemplateProcessor

template = TemplateManager(precompile=0).prepare(TEST + ".tmpl")
tproc = TemplateProcessor()
tproc.process(template)
