from django.urls import path
from . import views

urlpatterns = [
    path('footer/', views.footer, name='footer'),
]