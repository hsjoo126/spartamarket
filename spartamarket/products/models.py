from django.db import models
from django.conf import settings


class Products(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="product"
    )

    def __str__(self):
        return self.title