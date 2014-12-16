import io, sys, os, re

class maintenance():

	def __init__(self):
		self.validate = re.compile('20(\d{2}\-\d{2}\-\d{2})_.*\.(ogg|flac|wav)')

	def isValid(self,filename):
		return not self.validate.match(filename) is None