import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
	"""测试name_function.py"""
	def test_first_last_name(self):
		"""能够用正确地处理像James harden这样的名字吗？"""
		formatted_name=get_formatted_name('james','harden')
		self.assertEqual(formatted_name,'James Harden')
		
	def test_first_last_middle_name(self):
		"""能够正确地处理像Wolfgang Amadeus Mozart这样的姓名吗？"""
		formatted_name=get_formatted_name('wolfgang','mozart','amadeus')
		self.assertEqual(formatted_name,'Wolfgang Amadeus Mozart')

unittest.main()
