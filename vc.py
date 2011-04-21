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
	def __check(self, level):
		if level in self.verbosity:
			return True
		else:
			return False
	def __add_verbosity(self,verbosity):
		verbosity = int(verbosity)
		if not verbosity in VERBOSITY.keys():
			raise Exception()
		self.verbosity.append(verbosity)

	def add_verbosity(self, verbosity,cascade=False):
		try:
			try: verbosity = int(verbosity)
			except:
				pass
			if type(verbosity) == type(""):
				for k,v in VERBOSITY.items():
					if verbosity.lower() == v.lower():
						verbosity = k
						break
			if cascade:
				for i in VERBOSITY.keys():
					# add all levels below but don't add totally silent
					if i <= int(verbosity) and i != -1:
						self.__add_verbosity(i)
			else:
				self.__add_verbosity(verbosity)
		except Exception, e:
			raise
			sys.stderr.write("ERROR: Not a valid verbosity level \"%s\"\n" % str(verbosity))
			sys.exit(1)

	def clear_verbosity(self):
		self.verbosity = []
	def get_verbosity(self):
		return [ (i,VERBOSITY[i]) for i in self.verbosity ]
	def set_show_level(self, show_level):
		self.show_level = bool(level)
	def close(self):
		sys.stdout = sys.__stdout__
	def write(self, string):
		if self.__check(-1):
			return
		if string == '\n':
			return
		string += '\n'
		for i in STRINGS.keys():
			if string.startswith(STRINGS[i]+':'):
				if self.__check(i):
					if not self.show_level:
						string = string[len(STRINGS[i])+1:]
						if string[0] == ' ':
							string = string[1:]
					self.stdout.write(string)
					return
				return
		self.stdout.write(string)
		return

if __name__ == "__main__":
	if len(sys.argv) > 1:
		a = VerboseControl(sys.argv[1])
	else:
		a = VerboseControl(3)
	print "DEBUG: test1"
	print "INFO: test2"
	print "SUCCESS: test3"
	sys.__stdout__.write("Verbose Level: %s\n" % a.get_verbosity())
