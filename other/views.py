from datetime import datetime
from django.views import View
from django.http import HttpResponse
import random
from django.shortcuts import render
# from django.shortcuts import render

# Create your views here.


class CurrentDateView(View):
    def get(self, request):
        html = f"{datetime.now()}"
        return HttpResponse(html)


class RandomNum(View):
    def get(self, request):
        num = random.randint(1,5)
        return HttpResponse(num)


class IndexView(View):
    def get(self, request):
        return render(request, 'other/index.html')