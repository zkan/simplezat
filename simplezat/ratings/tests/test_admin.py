from django.test import TestCase

from ..admin import RatingAdmin


class RatingAdminTest(TestCase):
    def test_admin_should_register_rating_model(self):
        url = '/admin/ratings/rating/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_admin_should_show_defined_columns(self):
        expected = (
            'sentiment',
            'comment',
        )
        self.assertEqual(RatingAdmin.list_display, expected)
