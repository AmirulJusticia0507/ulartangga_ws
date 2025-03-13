from django.urls import path
from .views import home  # Ganti 'index' menjadi 'home'

urlpatterns = [
    path('', home, name='home'),  # Sesuaikan dengan nama fungsi di views.py
]
