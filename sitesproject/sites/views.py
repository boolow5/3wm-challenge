from django.shortcuts import render
from sites.models import *

# Create your views here.
def index(request):
    sites = Site.objects.all()
    context = {
      "sites": sites,
    }
    return render(request, "sites/index.html", context)

def site_detail(request, pk=None):
    site = Site.objects.get(pk=pk)
    items = Item.objects.filter(site__pk=pk)
    context = {
      "site": site,
      "items": items,
    }
    return render(request, "sites/details.html", context)