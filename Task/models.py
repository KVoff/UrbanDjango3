from django.db import models

class Article(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.author} on {self.created_at.strftime('%Y-%m-%d')}"
