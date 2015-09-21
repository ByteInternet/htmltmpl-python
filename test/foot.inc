
import codecs

output += tproc.process(template)

if "out" in sys.argv:
    sys.stdout.write(output)
    sys.exit(0)

res = codecs.open("%s.res" % TEST, 'r', encoding='utf-8').read()

print TEST, "...",

if output == res:
    print "OK"
else:
    print "FAILED"
    open("%s.fail" % TEST, "w").write(output.encode('utf-8'))
