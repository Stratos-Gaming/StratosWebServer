from django.db import models

# Create your models here.

class InstagramPost(models.Model):
    caption = models.TextField(blank=True, null=True)
    media_url = models.URLField(blank=True, null=True)  # For video URL
    img = models.URLField(blank=True, null=True)  # For image thumbnail
    timestamp = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"Post from {self.timestamp}"
