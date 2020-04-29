from django.shortcuts import render, redirect
from lists.models import Item, List


def home_page(request):
    """View for home page."""
    return render(request, 'home.html')


def view_list(request, list_id):
    """View for a list representation."""
    list_ = List.objects.get(id=list_id)
    return render(request, 'list.html', {'list': list_})


def new_list(request):
    """New list"""
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')


def add_item(request, list_id):
    """Add new element in list"""
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')
