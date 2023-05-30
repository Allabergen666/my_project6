from django.shortcuts import render
from .models import Contact

# Create your views here.

# views.py отвечает  на отправление и получение запроса с сайта

def index(request):
    all_data = Contact.objects.all()

    # render обновление сайта
    return render(request,  'home/index.html', {"context": all_data})

def add_index(request):
    return render(request, "block/index.html")
