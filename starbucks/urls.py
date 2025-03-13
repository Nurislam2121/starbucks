from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('delivery/', views.delivery, name='delivery'),
    path('home/', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('region/', views.region, name='region'),
    path('statement/', views.statement, name='statement'),
    path('products/<str:category>/', views.product_list_view, name='info'),
]

