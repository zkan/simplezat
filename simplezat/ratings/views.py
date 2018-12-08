from django.http import HttpResponse
from django.views import View


class RatingView(View):
    def get(self, request):
        return HttpResponse()
