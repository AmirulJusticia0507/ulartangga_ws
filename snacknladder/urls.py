from django.urls import path
from .views import index  # Ganti 'views' menjadi 'index'

urlpatterns = [
    path('', index, name='index'),  # Sesuaikan dengan nama fungsi di views.py
]
