import sys

class VerboseControl:
	def __init__(self,verbosity):
		self.verbosity = verbosity
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
