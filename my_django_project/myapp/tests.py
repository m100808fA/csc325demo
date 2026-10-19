from django.test import TestCase

# Create your tests here.

# create two test cases for the home and about views
class HomeViewTest(TestCase):
    def test_home_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

class AboutViewTest(TestCase):
    def test_about_view(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
        