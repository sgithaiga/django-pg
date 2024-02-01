from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from .models import *
# Create your views here.

def products(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "products.html", context)

def checkout(request):
    return render(request, "checkout.html")


class HomeView(ListView):
    model = Item
    template_name = "item_list.html"

class ItemDetailView(DetailView):
    model = Item
    template_name = "product.html"


