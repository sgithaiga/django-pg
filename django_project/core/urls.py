from django.urls import path
from .views import (
    HomeView,
    ItemDetailView,
    products,
    checkout
)



app_name = 'core'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('checkout/', checkout, name='checkout'),
    path('products/<slu>/', ItemDetailView.as_view(), name='products')
]