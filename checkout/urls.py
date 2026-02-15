from django.urls import path
from . import views

urlpatterns = [
    path('buy-now/<int:variant_id>/', views.buy_now, name='buy_now'),
    path('', views.checkout_page, name='checkout_page'),
    path('place-order/', views.place_order, name='place_order'),
    path('success/', views.payment_success, name='payment_success'),
]
