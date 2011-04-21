import sys

"""
Totally Silent: Output nothing. stderr will still be output
Silent: Only output Errors -> Use this level for when the program hits an
	urecoverable error
Warning: Only output Warnings -> Use this level for when the program hits a
	recoverable error
Normal: Just output text normally -> Use this for anything you want the user to
	see if they don't change the verbosity
Info: Output progress information -> Use this for telling the user the progress
	of actions
Verbose: Output everything -> Use this level for information which doesn't
	relate directly to the progress of the application but the user may
	still find useful
Debug: Output development information -> information for debugging the
	application. Probably only useful for developers

"""

VERBOSITY={ -1:'Totally Silent', 0:'Silent', 1:'Warning', 2:'Normal', 3:'Info', 4:'Verbose', 5:'Debug'}
STRINGS={ 0:'ERROR', 1:'WARNING', 3:'INFO', 4:'VERBOSE', 5:'DEBUG' }

class VerboseControl:
	"""Start a new Verbose Control

	Keyword arguments:
	verbosity -- verbosity level
	cascade -- verbosity level includes all levels below it
	show_level -- show the filter text

	"""
	def __init__(self,verbosity=None,cascade=True,show_level=False):
		self.clear_verbosity()
		if verbosity != None:
			self.add_verbosity(verbosity,cascade)
		self.show_level = show_level
		self.stdout = sys.__stdout__
		sys.stdout = self
	def __del__(self):
		self.close()
	def close(self):
		sys.stdout = sys.__stdout__
	def write(self, string):
		string += '\n'
		if string.startswith("DEBUG"):
			if (self.verbosity >= 5):
				self.stdout.write(string)
			return
		elif string.startswith("INFO"):
			if (self.verbosity >= 4):
				self.stdout.write(string)
			return
		elif string.startswith("SUCCESS"):
			if (self.verbosity >= 1):
				self.stdout.write(string)
			return
		elif string == '\n' or string == '\n\n':
			return
		else:
			self.stdout.write(string)
			return

if __name__ == "__main__":
	a = VerboseControl(3)
	print "DEBUG"
	print "INFO"
	print "SUCCESS"
