import sys
import os
import unittest
from singlelinkedlist import SingleLinkedList as sllist
class Basic_Test(unittest.TestCase):
	def setUp(self):
		Basic_Test.intial_list = [101, 200, 300]
		Basic_Test.test_list = sllist(*Basic_Test.intial_list)
	def test_str_method(self):
		"""
		Tests STR method overloading
		:return:
		"""
		self.assertEquals(str(Basic_Test.test_list) ,str(Basic_Test.intial_list))
	def test_len_method(self):
		"""
		Tests LEN method overloading
		:return:
		"""
		self.assertEquals(len(Basic_Test.test_list), len(Basic_Test.intial_list))
	def test_get_method(self):
		"""
		Tests get from index method overloading
		:return:
		"""
		self.assertEquals(Basic_Test.test_list[2], Basic_Test.intial_list[2])

	def test_append_method(self):
		test_item = 303
		Basic_Test.test_list.append(test_item)
		Basic_Test.intial_list.append(test_item)
		self.assertEquals(list(Basic_Test.test_list),
						  Basic_Test.intial_list)
if __name__ == '__main__':
	unittest.main()
