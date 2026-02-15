from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('living-room/', views.living_room, name='living_room'),
    path('bed-room/', views.bed_room, name='bed_room'),
    path('living-room/sofas/', views.sofa_list, name='sofa_list'),
    path('sofa/<slug:slug>/', views.sofa_detail, name='sofa_detail'),
    path('add-to-cart/<int:variant_id>/', views.add_to_cart, name='add_to_cart'),
    path('get-cart-items/', views.get_cart_items, name='get_cart_items'),
    path('get-cart-count/', views.get_cart_count, name='get_cart_count'),
    path("remove-cart-item/<int:item_id>/", views.remove_cart_item),



    path('search/', views.search, name='search'),  
    path('login/', views.login_view, name='login'),
    path("terms/", views.terms_view, name="terms"),

    
    path('logout/', views.logout_view, name='logout'),
    path("register/", views.register_view, name="register"),

   
    path('wishlist/add/<int:product_id>/', views.toggle_wishlist, name='toggle_wishlist'),
    

    path('living-room/curtains/', views.curtains_list, name='curtains_list'),
    path('curtains/<slug:slug>/', views.sofa_detail, name='curtains_detail'),
    
    path('living-room/centertable/', views.centertable_list, name='center table_list'),
    path('centertable/<slug:slug>/', views.sofa_detail, name='center table_detail'),

    path('living-room/carpets/', views.carpets_list, name='carpets_list'),
    path('carpets/<slug:slug>/', views.sofa_detail, name='carpets_detail'),
    
    path('living-room/tv_media_units/', views.tv_media_units_list, name='tv_media_units_list'),
    path('tv_media_units/<slug:slug>/', views.sofa_detail, name='tv_media_units_detail'),
    
    path('living-room/chairs/', views.chairs_list, name='chairs_list'),
    path('chairs/<slug:slug>/', views.sofa_detail, name='chairs_detail'),
    
    path('living-room/side-tables/', views.side_tables_list, name='side_tables_list'),
    path('side-tables/<slug:slug>/', views.sofa_detail, name='side-tables_detail'),
    
    path('living-room/cabinets-sideboards/', views.cabinets_sideboards_list, name='cabinets_sideboards_list'),
    path('cabinets-sideboards/<slug:slug>/', views.sofa_detail, name='cabinates-sideboards_detail'),
    
    path('living-room/wall-art-shelves/', views.wall_art_shelves_list, name='wall_art_shelves_list'),
    path('wall-art-shelves/<slug:slug>/', views.sofa_detail, name='wall-art-shelves_detail'),
    
    path('living-room/lighting/', views.lighting_list, name='lighting_list'),
    path('lighting/<slug:slug>/', views.sofa_detail, name='lighting_detail'),
    

]   


