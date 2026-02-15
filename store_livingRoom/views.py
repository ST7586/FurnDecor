from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Product,CartItem, ProductVariant, Wishlist
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages



def home(request):
    return render(request, 'store_livingRoom/home.html')


def living_room(request):
    return render(request, 'store_livingRoom/living_room.html')

def sofa_list(request):
    products = Product.objects.filter(category__iexact='sofa')
    return render(request, 'store_livingRoom/sofa_list.html', {'products': products})

def sofa_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    variants = ProductVariant.objects.filter(product=product)
    selected_variant = variants.first()

    is_wishlisted = False
    if request.user.is_authenticated:
        is_wishlisted = Wishlist.objects.filter(
            user=request.user,
            product=product
        ).exists()

    context = {
        'product': product,
        'variants': variants,
        'selected_variant': selected_variant,
        'is_wishlisted': is_wishlisted,   
    }
    return render(request, 'store_livingRoom/sofa_detail.html', context)



def add_to_cart(request, variant_id):
    variant = get_object_or_404(ProductVariant, id=variant_id)

    if not request.session.session_key:
        request.session.create()
    session_key = request.session.session_key

    # ✅ Fix here
    variant_name = variant.seater if variant.seater else "Standard"

    cart_item, created = CartItem.objects.get_or_create(
        session_key=session_key,
        product_name=variant.product.name,
        variant_name=variant_name,
        defaults={
            "image": variant.image,
            "new_price": variant.price,
            "old_price": variant.old_price,
        }
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    cart_count = CartItem.objects.filter(session_key=session_key).count()

    return JsonResponse({
        "status": "added",
        "cart_count": cart_count
    })



def get_cart_items(request):
    session_key = request.session.session_key
    items = CartItem.objects.filter(session_key=session_key)

    data = []
    for item in items:
        data.append({
            "id": item.id,
            "product": item.product_name,
            "variant": item.variant_name,
            "price": item.new_price,
            "image": item.image.url,
        })

    return JsonResponse({
        "items": data,
        "count": items.count()
    })


def get_cart_count(request):
    session_key = request.session.session_key
    if not session_key:
        return JsonResponse({"count": 0})

    count = CartItem.objects.filter(session_key=session_key).count()
    return JsonResponse({"count": count})
    

def remove_cart_item(request, item_id):
    CartItem.objects.filter(id=item_id).delete()
    return redirect(request.META.get("HTTP_REFERER", "/"))


def search(request):
    query = request.GET.get('q')

    if query:
        query = query.lower().strip()

        page_name = f"{query}_list"

        try:
            return redirect(page_name)
        except:
            return redirect('home')

    return redirect('home')




def toggle_wishlist(request, product_id):
    product = Product.objects.get(id=product_id)

    obj, created = Wishlist.objects.get_or_create(
        user=request.user if request.user.is_authenticated else None,
        product=product
    )

    if not created:
        obj.delete()
        added = False
    else:
        added = True

    count = Wishlist.objects.filter(
        user=request.user if request.user.is_authenticated else None
    ).count()

    return JsonResponse({
        "added": added,
        "count": count
    })


def login_view(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST["email"],
            password=request.POST["password"]
        )
        if user:
            login(request, user)
            return redirect("/")
    return render(request, "store_livingRoom/login.html")


def register_view(request):
    if request.method == "POST":
        User.objects.create_user(
            username=request.POST["email"],
            email=request.POST["email"],
            password=request.POST["password"],
            first_name=request.POST["first_name"],
            last_name=request.POST["last_name"],
        )
        return redirect("login")

    return render(request, "store_livingRoom/register.html")

def terms_view(request):
    return render(request, "store_livingRoom/terms.html")


def logout_view(request):
    logout(request)
    return redirect('home')


def curtains_list(request):
    products = Product.objects.filter(category__iexact='curtains')
    return render(request, 'store_livingRoom/curtains_list.html', {'products': products})

def curtains_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    
    is_wishlisted = False
    if request.user.is_authenticated:
        is_wishlisted = Wishlist.objects.filter(
            user=request.user,
            product=product
        ).exists()

    context = {
        'product': product,
    
        'is_wishlisted': is_wishlisted,   
    }
    return render(request, 'store_livingRoom/curtains_detail.html', context)

def centertable_list(request):
    products = Product.objects.filter(category__iexact='center table')
    return render(request, 'store_livingRoom/center table_list.html', {'products': products})

def centertable_detail(request, slug):   
    product = get_object_or_404(Product, slug=slug)
    variants = ProductVariant.objects.filter(product=product)
    selected_variant = variants.first()

    is_wishlisted = False
    if request.user.is_authenticated:
        is_wishlisted = Wishlist.objects.filter(
            user=request.user,
            product=product
        ).exists()

    context = {
        'product': product,
        'variants': variants,
        'selected_variant': selected_variant,
        'is_wishlisted': is_wishlisted,   
    }
    return render(request, 'store_livingRoom/center table_detail.html', context)
    
def carpets_list(request):
    products = Product.objects.filter(category__iexact='carpets')
    return render(request, 'store_livingRoom/carpets_list.html', {'products': products})

def carpets_detail(request, slug):   
    product = get_object_or_404(Product, slug=slug)
    variants = ProductVariant.objects.filter(product=product)
    selected_variant = variants.first()

    is_wishlisted = False
    if request.user.is_authenticated:
        is_wishlisted = Wishlist.objects.filter(
            user=request.user,
            product=product
        ).exists()

    context = {
        'product': product,
        'variants': variants,
        'selected_variant': selected_variant,
        'is_wishlisted': is_wishlisted,   
    }
    return render(request, 'store_livingRoom/carpets_detail.html', context)    

def tv_media_units_list(request):
    products = Product.objects.filter(category__iexact='tv & media units')
    return render(request, 'store_livingRoom/tv_media_units_list.html', {'products': products})

def tv_media_units_detail(request, slug):   
    product = get_object_or_404(Product, slug=slug)
    variants = ProductVariant.objects.filter(product=product)
    selected_variant = variants.first()

    is_wishlisted = False
    if request.user.is_authenticated:
        is_wishlisted = Wishlist.objects.filter(
            user=request.user,
            product=product
        ).exists()

    context = {
        'product': product,
        'variants': variants,
        'selected_variant': selected_variant,
        'is_wishlisted': is_wishlisted,   
    }
    return render(request, 'store_livingRoom/tv_media_units_detail.html', context)


def chairs_list(request):
    products = Product.objects.filter(category__iexact='chairs')
    return render(request, 'store_livingRoom/chairs_list.html', {'products': products})

def chairs_detail(request, slug):   
    product = get_object_or_404(Product, slug=slug)
    variants = ProductVariant.objects.filter(product=product)
    selected_variant = variants.first()

    is_wishlisted = False
    if request.user.is_authenticated:
        is_wishlisted = Wishlist.objects.filter(
            user=request.user,
            product=product
        ).exists()

    context = {
        'product': product,
        'variants': variants,
        'selected_variant': selected_variant,
        'is_wishlisted': is_wishlisted,   
    }
    return render(request, 'store_livingRoom/chairs_detail.html', context)    

def side_tables_list(request):
    products = Product.objects.filter(category__iexact='side tables')
    return render(request, 'store_livingRoom/side_tables_list.html', {'products': products})

def side_table_detail(request, slug):   
    product = get_object_or_404(Product, slug=slug)
    variants = ProductVariant.objects.filter(product=product)
    selected_variant = variants.first()

    is_wishlisted = False
    if request.user.is_authenticated:
        is_wishlisted = Wishlist.objects.filter(
            user=request.user,
            product=product
        ).exists()

    context = {
        'product': product,
        'variants': variants,
        'selected_variant': selected_variant,
        'is_wishlisted': is_wishlisted,   
    }
    return render(request, 'store_livingRoom/side_tables_detail.html', context)


def cabinets_sideboards_list(request):
    products = Product.objects.filter(category__iexact='cabinets & sideboards')
    return render(request, 'store_livingRoom/cabinets_sideboards_list.html', {'products': products})

def cabinets_detail(request, slug):   
    product = get_object_or_404(Product, slug=slug)
    variants = ProductVariant.objects.filter(product=product)
    selected_variant = variants.first()

    is_wishlisted = False
    if request.user.is_authenticated:
        is_wishlisted = Wishlist.objects.filter(
            user=request.user,
            product=product
        ).exists()

    context = {
        'product': product,
        'variants': variants,
        'selected_variant': selected_variant,
        'is_wishlisted': is_wishlisted,   
    }
    return render(request, 'store_livingRoom/cabinets_detail.html', context)    

def wall_art_shelves_list(request):
    products = Product.objects.filter(category__iexact='wall art & shelves')
    return render(request, 'store_livingRoom/wall_art_shelves_list.html', {'products': products})

def wall_art_shelves_detail(request, slug):   
    product = get_object_or_404(Product, slug=slug)
    variants = ProductVariant.objects.filter(product=product)
    selected_variant = variants.first()

    is_wishlisted = False
    if request.user.is_authenticated:
        is_wishlisted = Wishlist.objects.filter(
            user=request.user,
            product=product
        ).exists()

    context = {
        'product': product,
        'variants': variants,
        'selected_variant': selected_variant,
        'is_wishlisted': is_wishlisted,   
    }
    return render(request, 'store_livingRoom/wall_art_shelves_detail.html', context)    

def lighting_list(request):
    products = Product.objects.filter(category__iexact='lighting')
    return render(request, 'store_livingRoom/lighting_list.html', {'products': products})

def lighting_detail(request, slug):   
    product = get_object_or_404(Product, slug=slug)
    variants = ProductVariant.objects.filter(product=product)
    selected_variant = variants.first()

    is_wishlisted = False
    if request.user.is_authenticated:
        is_wishlisted = Wishlist.objects.filter(
            user=request.user,
            product=product
        ).exists()

    context = {
        'product': product,
        'variants': variants,
        'selected_variant': selected_variant,
        'is_wishlisted': is_wishlisted,   
    }
    return render(request, 'store_livingRoom/lighting_detail.html', context)






def bed_room(request):
    return render(request, 'store_livingRoom/bed_room.html')
