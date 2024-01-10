from django.views import View
from django.shortcuts import render


# Create your views here.
class CartView(View):
    def get(self, request):
        return render(request, 'store/cart.html')


class ProductView(View):
    def get(self, request):
        return render(request, 'store/product-single.html')


class ShopView(View):
    def get(self, request):
        return render(request, 'store/shop.html')
