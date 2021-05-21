from django.test import SimpleTestCase

# Create your tests here.
class SimpleTest(SimpleTestCase):
    def test_home_page_status_coded(self):
        response = self.client.get('/ch1/')

        self.assertEqual(response.status_code,200)

    def test_about_page_status_coded(self):

        response = self.client.get('/ch1/about/')

        self.assertEqual(response.status_code,200)