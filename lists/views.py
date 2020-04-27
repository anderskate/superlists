from django.shortcuts import render


def home_page(request):
    """View for home page."""
    return render(request, 'home.html')

