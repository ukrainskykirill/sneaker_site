from django.db import models
from django.urls import reverse


class Sneaker(models.Model):
    sneaker = models.CharField(max_length=30, verbose_name="Кроссовки")
    brands = models.ManyToManyField("Brand", verbose_name="Бренд")
    slug = models.SlugField(
        max_length=255, unique=True, db_index=True, verbose_name="URL"
    )
    photo = models.ImageField(upload_to="photos_of_sneaker/%Y/%m/%d")
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Цена")
    sizes = models.ManyToManyField("Size", verbose_name="Размер")
    articles = models.ForeignKey(
        "Article", on_delete=models.PROTECT, verbose_name="Статьи"
    )

    def __str__(self):
        return self.sneaker

    class Meta:
        verbose_name = "Кроссовки"
        verbose_name_plural = "Кроссовки"

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"id": self.id, "slug": self.slug})


class Feedback(models.Model):
    sneaker = models.ForeignKey(
        "Sneaker", on_delete=models.PROTECT, null=True, verbose_name="Кроссовки"
    )
    feedback = models.CharField(max_length=5000, verbose_name="Отзыв")

    class Meta:
        verbose_name = "Отзывы"
        verbose_name_plural = "Отзывы"


class Size(models.Model):
    size_num = models.IntegerField()

    def __str__(self):
        n = str(self.size_num)
        return n

    class Meta:
        verbose_name = "Размеры"
        verbose_name_plural = "Размеры"


class Article(models.Model):
    title = models.CharField(max_length=300, verbose_name="Заголовок")
    text = models.TextField(max_length=10000, verbose_name="Содержание")
    photo = models.ImageField(
        upload_to="photos_of_article/%Y/%m/%d", verbose_name="Фото"
    )
    slug = models.SlugField(
        max_length=255, unique=True, db_index=True, verbose_name="URL"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Статьи"
        verbose_name_plural = "Статьи"

    def get_absolute_url(self):
        return reverse("show_post", kwargs={"post_slug": self.slug})


class Brand(models.Model):
    brand_name = models.CharField(max_length=50)

    def __str__(self):
        return self.brand_name

    class Meta:
        verbose_name = "Бренды"
        verbose_name_plural = "Бренды"
