from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('who-we-are/', views.who_we_are, name='who_we_are'),
    path('what-we-do/', views.what_we_do, name='what_we_do'),
    path('contact/', views.contact, name='contact'),
    path('sitemap/', views.sitemap, name='sitemap'),
    path('cancellation-policy/', views.cancellation_policy, name='cancellation_policy'),
    path('warranty/', views.warranty_policy, name='warranty_policy'),
    path('faqs/', views.faqs, name='faqs'),
    path("store-locator/", views.store_locator, name="store_locator"),


]
