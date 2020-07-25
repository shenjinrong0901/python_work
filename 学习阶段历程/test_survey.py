import unittest
from survery import AnonymousSurvery

class TestAnonmyousSurvey(unittest.TestCase):
	
	def test_store_single_response(self):
		"""测试单个的答案会被妥善地存储"""
		question="What language did you first learn to speak?"
		my_survery=AnonymousSurvery(question)
		my_survery.store_response('English')
		
		self.assertIn('English',my_survery.responses)
		
unittest.main()
