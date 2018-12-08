from django.urls import path

from .views import (
    CommentView,
    RatingView,
    ThanksView,
)


urlpatterns = [
    path('', RatingView.as_view(), name='ratings'),
    path('thanks/', ThanksView.as_view(), name='thanks'),
    path('<str:rating>/', CommentView.as_view(), name='comments'),
]
