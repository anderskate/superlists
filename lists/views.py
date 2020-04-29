from django.shortcuts import render, redirect
from lists.models import Item, List


def home_page(request):
    """View for home page."""
    return render(request, 'home.html')


def view_list(request):
    """View for a list representation."""
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})


def new_list(request):
    """New list"""
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/one_list_in_the_world/')
