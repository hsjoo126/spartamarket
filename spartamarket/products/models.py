from django.db import models
from django.conf import settings


class Products(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()

    author = models.ForeignKey( #유저테이블이랑 포린키로 이미 엮여있다! ;;;
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="product"
    )

    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="like_products"
    )
    def __str__(self):
        return self.title