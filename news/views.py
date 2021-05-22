from django.shortcuts import render
from .models import Items

def index(request):
    items_list = Items.objects.all()
    data = {}
    tmp = []
    for el in items_list:
        tmp.append(el)
    data['names'] = tmp
    return render(request, 'main.html', context=data)

def contacts(request):
    return render(request, 'contacts.html')
def delivery(request):
    return render(request, 'delivery.html')
def login(request):
    return render(request, 'login.html')
def gadget(request):
    return render(request, 'gadget.html')