from django.urls import path
from .views import CartView, ProductView, ShopView

# app_name = "store"

urlpatterns = [
    path('', ShopView.as_view(), name="shop"),
    path('cart/', CartView.as_view(), name="cart"),
    path('product/', ProductView.as_view())
]