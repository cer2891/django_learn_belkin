from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True,
                             verbose_name='Наименование категории')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']

    def get_absolute_url(self):
        return reverse('category', kwargs={"category_id": self.pk})

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Содержание')
    create_at = models.DateTimeField(auto_now_add=True,
                                     verbose_name='дата создания')
    update_at = models.DateTimeField(auto_now=True, verbose_name='обновленно')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True,
                              verbose_name='фото')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовать ?')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True,
                                 verbose_name='Категория')
    views = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('view_news', kwargs={"pk": self.pk})

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-create_at']
