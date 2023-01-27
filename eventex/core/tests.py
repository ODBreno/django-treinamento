from django.test import TestCase

# Create your tests here.

def setUp(self):
    self.response = self.client.get('/')

class HomeTest(TestCase):
    def test_get(self):
        """GET / must return status code 200"""

        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must use index.html"""

        self.assertTemplateUsed(self.response, 'index.html')
