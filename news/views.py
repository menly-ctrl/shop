from django.shortcuts import render
from .models import Item

def index(request):
    items_query = Item.objects.all()
    items_list = []

    for el in items_query:
        tmp = []
        tmp.append(el.image)
        tmp.append(el.item_name)
        tmp.append(el.item_description)
        tmp.append(el.item_price)
        items_list.append(tmp)
    data = {
        'items' : items_list,
    }

    return render(request, 'main.html', context=data)


def contacts(request):
    return render(request, 'contacts.html')
def delivery(request):
    return render(request, 'delivery.html')
def login(request):
    return render(request, 'login.html')
def gadget(request):
    return render(request, 'gadget.html')