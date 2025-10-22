from django.db import models

class Brand(models.Model):
    name = models.CharField(verbose_name="Наименование", max_length=255, null=False, blank=False)
    country = models.CharField(verbose_name="Страна", max_length=255, null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = "Бренд"
        verbose_name_plural = "Бренды"

class Category(models.Model):
    name = models.CharField(verbose_name="Наименование", max_length=255, null=False, blank=False)
    parent_category = models.ForeignKey("self", verbose_name="Родительская категория", null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Product(models.Model):
    name = models.CharField(verbose_name="Наименование", max_length=255, null=False, blank=False)
    description = models.TextField(verbose_name="Описание", max_length=1000, null=False, blank=False)
    price = models.DecimalField(verbose_name="Цена", decimal_places=2, max_digits=9, null=False, blank=False)
    image_url = models.URLField(verbose_name="Ссылка на изображение", max_length=500, null=False, blank=False)
    category = models.ForeignKey("Category", verbose_name="Категория",null=False, blank=False, on_delete=models.CASCADE)
    brand = models.ForeignKey("Brand", verbose_name="Бренд", null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"