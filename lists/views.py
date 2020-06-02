from django.shortcuts import render, redirect
from lists.models import Item, List
from django.core.exceptions import ValidationError


def home_page(request):
    """View for home page."""
    return render(request, 'home.html')


def view_list(request, list_id):
    """View for a list representation."""
    list_ = List.objects.get(id=list_id)
    error = None
    if request.method == 'POST':
        try:
            item = Item(text=request.POST['item_text'], list=list_)
            item.full_clean()
            item.save()
            return redirect(f'/lists/{list_.id}/')
        except ValidationError:
            error = 'You cant have an empty list item'
    return render(request, 'list.html', {'list': list_, 'error': error})


def new_list(request):
    """New list"""
    list_ = List.objects.create()
    item = Item(text=request.POST['item_text'], list=list_)
    try:
        item.full_clean()
        item.save()
    except ValidationError:
        list_.delete()
        error = 'You cant have an empty list item'
        return render(request, 'home.html', {'error': error})
    return redirect(f'/lists/{list_.id}/')

