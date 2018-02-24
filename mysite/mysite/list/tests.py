from django.test import TestCase

# Create your tests here.
from django.core.urlresolvers import resolve
from list.views import home_page

class testcase(TestCase):
	def test_resolve(self):
		found = resolve("/")
		self.assertEqual(found.func,home_page)
