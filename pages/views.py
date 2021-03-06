from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from listings.models import Listing
from realtors.models import Realtor


def index(req):
    listings = Listing.objects.order_by(
        '-list_date').filter(is_published=True)[:3]
    context = {
        'listings':listings
    }
    return render(req, 'pages/index.html', context)


def about(req):
    # Get all realtors
    realtor = Realtor.objects.order_by('-hire_date')

    # Get MVP 
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors':realtor,
        'mvp_realtors':mvp_realtors
    }

    return render(req, 'pages/about.html',context)
