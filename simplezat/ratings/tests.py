from django.urls import reverse
from django.test import TestCase


class RatingViewTest(TestCase):
    def setUp(self):
        self.url = reverse('ratings')

    def test_rating_view_should_have_question_text(self):
        response = self.client.get(self.url)

        expected = '<h1>How do we do?</h1>'
        self.assertContains(response, expected, status_code=200)

    def test_rating_view_should_show_three_ratings(self):
        response = self.client.get(self.url)

        positive_url = reverse('comments', kwargs={'rating': 'positive'})
        expected = f'<a href="{positive_url}">' \
            '<img src="/static/images/positive.png" alt="Positive"></a>'
        self.assertContains(response, expected, status_code=200)

        neutral_url = reverse('comments', kwargs={'rating': 'neutral'})
        expected = f'<a href="{neutral_url}">' \
            '<img src="/static/images/neutral.png" alt="Neutral"></a>'
        self.assertContains(response, expected, status_code=200)

        negative_url = reverse('comments', kwargs={'rating': 'negative'})
        expected = f'<a href="{negative_url}">' \
            '<img src="/static/images/negative.png" alt="Negative"></a>'
        self.assertContains(response, expected, status_code=200)


class CommentViewTest(TestCase):
    def test_comment_view_should_render_text_and_comment_form_correctly(self):
        for each in ['positive', 'abc', 'xyz']:
            url = reverse(
                'comments',
                kwargs={
                    'rating': each
                }
            )
            response = self.client.get(url)

            expected = '<h1>Any comment?</h1>'
            self.assertContains(response, expected, status_code=200)

            expected = '<form action="." method="post">' \
                '<input type="hidden" name="csrfmiddlewaretoken"'
            self.assertContains(response, expected, status_code=200)

            expected = '<textarea name="comment"></textarea>' \
                f'<input type="hidden" name="rating" value="{each}">' \
                '<button type="submit">Submit</button></form>'
            self.assertContains(response, expected, status_code=200)

    def test_submit_comment_form_should_redirect_to_thanks_page(self):
        url = reverse(
            'comments',
            kwargs={
                'rating': 'positive'
            }
        )
        response = self.client.post(url)
        self.assertRedirects(response, reverse('thanks'))


class ThanksViewTest(TestCase):
    def test_thanks_view_should_render_thank_you_text(self):
        url = reverse('thanks')
        response = self.client.get(url)

        expected = '<h1>Thank You!</h1>'
        self.assertContains(response, expected, status_code=200)
