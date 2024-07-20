from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from hodimlar.models import Hodim


def home(request):
    hodimlar = Hodim.objects.all()
    context = {
        'hodimlar': hodimlar
    }
    return render(request, "main.html",context)