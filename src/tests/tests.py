import unittest, io, sys, os
sys.path.append( os.path.abspath('..' ) )
from maintenance import maintenance

class maintenanceTests(unittest.TestCase):
	def setUp(self):
		self.inst = maintenance()

	def test_invalid_format(self):
		self.assertFalse(self.inst.isValid('Super-Promo-Le-Mardi.mp3'))
		self.assertFalse(self.inst.isValid('Super-Promo-Le-Mardi.ogg'))
		self.assertFalse(self.inst.isValid('Super-Promo-Le-Mardi.wav'))

	def test_valid_format(self):
		self.assertTrue(self.inst.isValid('2014-03-03_Super-Promo-Le-Mardi.ogg'))
		self.assertTrue(self.inst.isValid('2014-03-03_Super-Promo-Le-Mardi.flac'))
		self.assertTrue(self.inst.isValid('2014-03-03_Super-Promo-Le-Mardi.wav'))

	def test_valid_format_but_invalid_codec(self):
		self.assertFalse(self.inst.isValid('2014-03-03_Super-Promo-Le-Mardi.mp3'))
		self.assertFalse(self.inst.isValid('2014-03-03_Super-Promo-Le-Mardi.laac'))
		self.assertFalse(self.inst.isValid('2014-03-03_Super-Promo-Le-Mardi.aac'))

if __name__ == '__main__':
	unittest.main()