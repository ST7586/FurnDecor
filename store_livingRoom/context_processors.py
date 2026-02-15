from .models import Wishlist

def wishlist_count(request):
    if request.user.is_authenticated:
        items = Wishlist.objects.filter(user=request.user)
    else:
        items = Wishlist.objects.filter(user__isnull=True)

    return {
        'wishlist_count': items.count(),
        'wishlist_items': items   
    }
