from django.shortcuts import render
from .models import ContactQuery

# Create your views here.

def about(request):
    return render(request, 'pages/about.html')

def who_we_are(request):
    return render(request, 'pages/who_we_are.html')

def what_we_do(request):
    return render(request, 'pages/what_we_do.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        query = request.POST.get('query')

        ContactQuery.objects.create(
            name=name,
            phone=phone,
            query=query
        )

    return render(request, 'pages/contact.html')


def sitemap(request):
    return render(request, 'pages/sitemap.html')

def cancellation_policy(request):
    return render(request, 'pages/cancellation_policy.html')

def warranty_policy(request):
    return render(request, 'pages/warranty_policy.html')

def faqs(request):
    return render(request, 'pages/faqs.html')

def store_locator(request):
    stores = {
        "Aurangabad": [
            {
                "name": "FurnDecor – CIDCO",
                "address": "Plot No. 12, CIDCO Town Centre, Aurangabad, Maharashtra 431003",
                "phone": "+91 91234 56701",
                "timing": "10:30 AM – 9:30 PM"
            }
        ],

        "Ahmedabad": [
            {
                "name": "FurnDecor – SG Highway",
                "address": "Ground Floor, SG Highway, Ahmedabad, Gujarat 380015",
                "phone": "+91 91234 56702",
                "timing": "10:00 AM – 9:30 PM"
            }
        ],

        "Bhubaneswar": [
            {
                "name": "FurnDecor – Nayapalli",
                "address": "Nayapalli Main Road, Bhubaneswar, Odisha 751012",
                "phone": "+91 91234 56706",
                "timing": "10:00 AM – 9:00 PM"
            }
        ],

        "Guwahati": [
            {
                "name": "FurnDecor – GS Road",
                "address": "GS Road, Dispur, Guwahati, Assam 781006",
                "phone": "+91 91234 56707",
                "timing": "10:30 AM – 9:30 PM"
            }
        ],

        "Hyderabad": [
            {
                "name": "FurnDecor – Gachibowli",
                "address": "Financial District Road, Gachibowli, Hyderabad 500032",
                "phone": "+91 91234 56704",
                "timing": "10:30 AM – 9:30 PM"
            }
        ],

        "Kolkata": [
            {
                "name": "FurnDecor – Salt Lake",
                "address": "Sector V, Salt Lake, Kolkata 700091",
                "phone": "+91 91234 56705",
                "timing": "11:00 AM – 9:00 PM"
            }
        ],

        "Lucknow": [
            {
                "name": "FurnDecor – Gomti Nagar",
                "address": "Vibhuti Khand, Gomti Nagar, Lucknow, Uttar Pradesh 226010",
                "phone": "+91 91234 56708",
                "timing": "10:00 AM – 9:30 PM"
            }
        ],

        "Nagpur": [
            {
                "name": "FurnDecor – Wardha Road",
                "address": "Wardha Road, Nagpur, Maharashtra 440015",
                "phone": "+91 91234 56709",
                "timing": "10:30 AM – 9:30 PM"
            }
        ],

        "Nashik": [
            {
                "name": "FurnDecor – College Road",
                "address": "College Road, Nashik, Maharashtra 422005",
                "phone": "+91 91234 56710",
                "timing": "10:00 AM – 9:00 PM"
            }
        ],

        "Patna": [
            {
                "name": "FurnDecor – Bailey Road",
                "address": "Bailey Road, Patna, Bihar 800014",
                "phone": "+91 91234 56711",
                "timing": "10:30 AM – 9:00 PM"
            }
        ],

        "Pune": [
            {
                "name": "FurnDecor – Wakad",
                "address": "Near Hinjewadi Flyover, Wakad, Pune, Maharashtra 411057",
                "phone": "+91 91234 56703",
                "timing": "10:00 AM – 9:30 PM"
            }
        ],

        "Raipur": [
            {
                "name": "FurnDecor – Pandri",
                "address": "Pandri Market Area, Raipur, Chhattisgarh 492004",
                "phone": "+91 91234 56712",
                "timing": "10:00 AM – 9:00 PM"
            }
        ],

        "Siliguri": [
            {
                "name": "FurnDecor – Sevoke Road",
                "address": "Sevoke Road, Siliguri, West Bengal 734001",
                "phone": "+91 91234 56713",
                "timing": "10:30 AM – 9:00 PM"
            }
        ],

        "Visakhapatnam": [
            {
                "name": "FurnDecor – MVP Colony",
                "address": "MVP Colony, Visakhapatnam, Andhra Pradesh 530017",
                "phone": "+91 91234 56714",
                "timing": "10:00 AM – 9:30 PM"
            }
        ],
    }

    return render(request, "pages/store_locator.html", {"stores": stores})

