from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item


def home_page(request):
    """View for home page."""
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/lists/one_list_in_the_world/')
    return render(request, 'home.html')


def view_list(request):
    """View for a list representation."""
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})
