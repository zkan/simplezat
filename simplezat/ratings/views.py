from django.shortcuts import render
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


class ThanksView(TemplateView):
    template = 'thanks.html'

    def get(self, request):
        return render(
            request,
            self.template
        )
