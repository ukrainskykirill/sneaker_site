from django.urls import path
from .views import *

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("goods/", Buy.as_view(), name="buy"),
    path("support/", Support.as_view(), name="support"),
    path("contact", Contact.as_view(), name="contact"),
    path("review/", Review.as_view(), name="review"),
    path("review/<slug:post_slug>/", ShowPost.as_view(), name="show_post"),
    path("feedback/", AddFeedback.as_view(), name="feedback"),
    path("api/v1/article/", ArticleAPIView.as_view()),
    path("api/v1/review/<int:pk>/", ArticleUpdate.as_view()),
]
