from django.urls import reverse
from django.test import TestCase


class RatingViewTest(TestCase):
    def test_rating_view_should_be_accessible(self):
        url = reverse('ratings')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
