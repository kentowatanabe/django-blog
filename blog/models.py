from django.db import models
from django.utils import timezone


class Category(models.Model):
    """Post Category."""

    name = models.CharField('Category Name', max_length=255)
    created_at = models.DateTimeField('Create Date', default=timezone.now)

    def __str__(self):
        return self.name


class Post(models.Model):
    """Post."""

    title = models.CharField('Title', max_length=255)
    text = models.TextField('Text')
    category = models.ForeignKey(
        Category, verbose_name='Category', on_delete=models.PROTECT
    )
    created_at = models.DateTimeField('Create Date', default=timezone.now)

    def __str__(self):
        return self.title


class Comment(models.Model):
    """Comment."""

    name = models.CharField('Name', max_length=30, blank=True, default='anonymous')
    text = models.TextField('Comment')
    post = models.ForeignKey(
        Post, verbose_name='Post', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField('Create Date', default=timezone.now)

    def __str__(self):
        return self.text[:10]
