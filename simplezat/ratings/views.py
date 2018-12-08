from django.urls import reverse
from django.shortcuts import (
    redirect,
    render,
)
from django.views.generic import TemplateView


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
        return render(
            request,
            self.template,
            {
                'rating': rating
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
