from django.db import models
from django.utils import timezone


class Post(models.Model):
    class StatusChoices(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    body = models.TextField()
    published_at = models.DateTimeField(default=timezone.now())
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,
                              choices=StatusChoices.choices,
                              default=StatusChoices.DRAFT)

    class Meta:
        ordering = ('-published_at', )
        indexes = [
            models.Index(fields=['published_at'], name='publish')
        ]

    def __str__(self):
        return self.title
