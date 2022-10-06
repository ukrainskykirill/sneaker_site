menu = [
    {"title": "Главная", "url_name": "home"},
    {"title": "Обзор", "url_name": "review"},
    {"title": "Товары", "url_name": "buy"},
    {"title": "Контакты", "url_name": "contact"},
    {"title": "Поддержка", "url_name": "support"},
    {"title": "Оставить отзыв", "url_name": "feedback"},
]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context["menu"] = menu
        return context
