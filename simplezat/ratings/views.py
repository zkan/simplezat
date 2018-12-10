from django.urls import reverse
from django.shortcuts import (
    redirect,
    render,
)
from django.views.generic import TemplateView

from .forms import RatingForm


class RatingView(TemplateView):
    template = 'ratings.html'

    def get(self, request):
        return render(
            request,
            self.template
        )


class CommentView(TemplateView):
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


class ThanksView(TemplateView):
    template = 'thanks.html'

    def get(self, request):
        return render(
            request,
            self.template
        )
