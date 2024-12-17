from django.db import models
from django.db.models import AutoField


#  your models here.
class Categories(models.Model):
    cat_id = models.CharField(unique=True, max_length=200, null=True, blank=True)
    name =models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Advertisement(models.Model):
    ad_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='advertisement_images/img')

    def __str__(self):
        return self.name

class Article(models.Model):
    STATUS_CHOICES = [
        ('P', 'Published'),
        ('U', 'Unpublished'),
    ]

    a_id = models.AutoField(primary_key=True)  # Custom primary key
    image = models.ImageField(upload_to='article_images/img')
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=200, null=True, blank=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='U')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    views_count = models.IntegerField(default=0)
    cat_id = models.ForeignKey(
        'Categories',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title


class Image(models.Model):
    img_id = AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='single_images/img')
    album_id = models.ForeignKey(
        'Categories',
        on_delete=models.CASCADE
    )
    def __str__(self):
        return self.name