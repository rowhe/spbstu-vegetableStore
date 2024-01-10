from django.urls import path
from .views import LoginUrl

urlpatterns = [
    path('', LoginUrl.as_view())
]