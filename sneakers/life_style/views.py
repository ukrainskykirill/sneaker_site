from rest_framework.generics import CreateAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from cart.forms import CartAddProductForm


from django.forms import forms, model_to_dict
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from .serializers import ArticleSerializer
from .utils import DataMixin

from .forms import AddFeedbackForm
from .models import *
from rest_framework import generics


class Home(DataMixin, ListView):
    model = Sneaker
    template_name = "life_style/home.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        cntxt = self.get_user_context(title="Главная страница")
        return dict(list(context.items()) + list(cntxt.items()))


class Buy(DataMixin, ListView):
    model = Sneaker
    context_object_name = "goods"
    template_name = "life_style/buy.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cntxt = self.get_user_context(title="Товары")
        return dict(list(context.items()) + list(cntxt.items()))


class Review(DataMixin, ListView):
    model = Article
    context_object_name = "article"
    template_name = "life_style/review.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cntxt = self.get_user_context(title="Обзор")
        return dict(list(context.items()) + list(cntxt.items()))


class ShowPost(DataMixin, DetailView):
    model = Article
    slug_url_kwarg = "post_slug"
    context_object_name = "post"
    template_name = "life_style/article.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cntxt = self.get_user_context(title="Обзор")
        return dict(list(context.items()) + list(cntxt.items()))


class AddFeedback(DataMixin, CreateView):
    form_class = AddFeedbackForm
    template_name = "life_style/feedback.html"
    success_url = reverse_lazy("feedback")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cntxt = self.get_user_context(title="Оставь свой отзыв")
        return dict(list(context.items()) + list(cntxt.items()))


class Contact(DataMixin, ListView):
    model = Article
    template_name = "life_style/contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cntxt = self.get_user_context(title="Контакты")
        return dict(list(context.items()) + list(cntxt.items()))


class Support(DataMixin, ListView):
    model = Article
    template_name = "life_style/support.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cntxt = self.get_user_context(title="Поддержка")
        return dict(list(context.items()) + list(cntxt.items()))


def product_detail(request, id, slug):
    product = get_object_or_404(Sneaker, id=id, slug=slug,)
    cart_product_form = CartAddProductForm()
    return render(
        request,
        "life_style/buy.html",
        {"product": product, "cart_product_form": cart_product_form},
    )


class ArticleAPIView(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleUpdate(generics.UpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    # def get(self, request):
    #     w = Article.objects.all()
    #     return Response({'posts': ArticleSerializer(w, many=True).data})
    #
    # def post(self, request):
    #     # добавим проверку
    #     serializer = ArticleSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #
    #     post_new = Article.objects.create\
    #             (
    #         title = request.data['title'],
    #         text = request.data['text'],
    #         slug = request.data['slug']
    #         )
    #     return Response({'post': ArticleSerializer(post_new, many=True).data})
