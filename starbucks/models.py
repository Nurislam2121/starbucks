from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('napitki', 'Напитки'),
        ('eda', 'Еда'),
        ('stakany', 'Стаканы'),
        ('zerno_kofe', 'Зерна кофе'),
    ]
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)


    def __str__(self):
        return self.name

