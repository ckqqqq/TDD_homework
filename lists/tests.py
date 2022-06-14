from django.test import TestCase
# Create your tests here.

class HomepageTest(TestCase):
    def test_uses_home_template(self):
        response = self.clinet.get('/')
        self.assertTemplateUsed(response, 'home.html')