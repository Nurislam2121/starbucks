from django.shortcuts import render
from .models import Product

def about(request):
    return render(request, 'about.html')

def delivery(request):
    return render(request, 'delivery.html')

def footer(request):
    return render(request, 'footer.html')

def header(request):
    return render(request, 'header.html')

def home(request):
    return render(request, 'home.html')

def info(request):
    return render(request, 'info.html')

def menu(request):
    return render(request, 'menu.html')

def region(request):
    return render(request, 'region.html')

def statement(request):
    return render(request, 'statement.html')




def product_list_view(request, category):
    products = Product.objects.filter(category=category)
    
    if category == 'napitki':
        heading = "Весенние новинки уже в кофейнях!"
        subheading = "Наслаждайтесь напитками Starbucks"
        description = "При таком богатстве выбора самый лучший способ найти свой любимый кофе – это попробовать каждый"
    elif category == 'eda':
        heading = "Еда"
        subheading = "Попробуйте нашу вкусную еду"
        description = "Наша выпечка и сэндвичи готовятся из высококачественных и простых ингредиентов. Поэтому все, что вы пробуете, - настоящая и действительно вкусная еда"
    elif category == 'stakany':
        heading = "Стаканы и Тамблеры"
        subheading = "Найдите идеальный аксессуар для вашего напитка"
        description = "Удобные и яркие кружки, тамблеры, бутылки для воды и другое."
    elif category == 'zerno_kofe':
        heading = "Зерна Кофе"
        subheading = "Наше кофе с заботой и вниманием к каждой детали"
        description = "Мы предлагаем лучшие сорта зернового кофе, произведенные в лучших регионах мира, чтобы вы наслаждались уникальными вкусами в каждом глотке."
    
    context = {
        'products': products,
        'heading': heading,
        'subheading': subheading,
        'description': description,
    }
    return render(request, 'info.html', context)
