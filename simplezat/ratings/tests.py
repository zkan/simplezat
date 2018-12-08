from django.test import TestCase


class RatingViewTest(TestCase):
    def test_rating_view_should_be_accessible(self):
        response = self.client.get('/ratings/')
        self.assertEqual(response.status_code, 200)
