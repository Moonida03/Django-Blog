from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_query(self):
        return super().get_queryset().filter(status='PB')


class Post(models.Model):
    class StatusChoices(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique_for_date='published_at')
    body = models.TextField()
    published_at = models.DateTimeField(default=timezone.now())
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,
                              choices=StatusChoices.choices,
                              default=StatusChoices.DRAFT)
    auther = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='posts')
    objects = models.Manager()
    published = PublishedManager()

    def get_absolute_url(self):
        return reverse('post-detail', args=[self.published_at.year,
                                            self.published_at.month,
                                            self.published_at.day,
                                            self.slug])

    class Meta:
        ordering = ('-published_at', )
        indexes = [
            models.Index(fields=['published_at'], name='publish')
        ]

    def __str__(self):
        return self.title
