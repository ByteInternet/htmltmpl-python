
output += tproc.process(template)

if "out" in sys.argv:
    sys.stdout.write(output)
    sys.exit(0)

res = open("%s.res" % TEST).read()

print TEST, "...",

if output == res:
    print "OK"
else:
    print "FAILED"
    print output
    open("%s.fail" % TEST, "w").write(output)
