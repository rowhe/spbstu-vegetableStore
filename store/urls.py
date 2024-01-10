from django.urls import path
from .views import CartView, ProductView, ShopView

urlpatterns = [
    path('', ShopView.as_view()),
    path('cart/', CartView.as_view()),
    path('product/', ProductView.as_view())
]