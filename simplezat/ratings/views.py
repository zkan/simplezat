from django.urls import reverse
from django.shortcuts import (
    redirect,
    render,
)
from django.views import View

from .forms import RatingForm


class RatingView(View):
    template = 'ratings.html'

    def get(self, request):
        return render(
            request,
            self.template
        )


class CommentView(View):
    template = 'comments.html'

    def get(self, request, rating):
        initial = {
            'sentiment': rating
        }
        form = RatingForm(initial=initial)

        return render(
            request,
            self.template,
            {
                'rating': rating,
                'form': form
            }
        )

    def post(self, request, rating):
        return redirect(reverse('thanks'))


class ThanksView(View):
    template = 'thanks.html'

    def get(self, request):
        return render(
            request,
            self.template
        )
