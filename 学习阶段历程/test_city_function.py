import unittest
from city_functions import get_formatted_name

class NameTestCase(unittest.TestCase):
	def test_city_country_name(self):
		city_name=get_formatted_name('上海','中国')
		self.assertEqual(city_name,'上海 中国')
		
unittest.main()
