# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from store_livingRoom.models import ProductVariant
from .models import Order

def buy_now(request, variant_id):
    variant = get_object_or_404(ProductVariant, id=variant_id)

    request.session['buy_now'] = {
        'variant_id': variant.id,
        'name': variant.product.name,
        'price': float(variant.price),
        'image': variant.image.url   # ✅ correct line
    }

    return redirect('checkout_page')



def checkout_page(request):
    product = request.session.get('buy_now')
    return render(request, 'checkout/checkout.html', {'product': product})


def place_order(request):
    if request.method == "POST":
        product = request.session.get('buy_now')

        order = Order.objects.create(
            variant_id = product['variant_id'],
            product_name = product['name'],
            price = product['price'],
            mobile = request.POST.get('mobile'),
            pincode = request.POST.get('pincode'),
            city = request.POST.get('city'),
            state = request.POST.get('state'),
            address = request.POST.get('address'),
            payment_method = request.POST.get('payment_method'),
            is_paid = True
        )

        return redirect('payment_success')


def payment_success(request):
    return render(request, 'checkout/payment_success.html')
