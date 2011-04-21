from vc import VerboseControl

e = VerboseControl(3)
print "DEBUG: boom"
print "INFO: boom"
print "boom"
print e.get_verbosity()
