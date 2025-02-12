from django.db import models


class Books(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    content = models.TextField(default='')
    author = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13)
    price = models.DecimalField(max_digits=100, decimal_places=2) # 999.99

    def __str__(self):
        return self.title