from django.urls import path
from .views import CurrentDateView, RandomNum, IndexView

urlpatterns = [
    path('datetime/', CurrentDateView.as_view()),
    path('rand/', RandomNum.as_view()),
    path('', IndexView.as_view()),
]