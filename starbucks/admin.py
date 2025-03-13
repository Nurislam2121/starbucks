from django.contrib import admin
from .models import Product  # Импортируйте вашу модель

admin.site.register(Product)  # Регистрируйте модель
