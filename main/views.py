from django.shortcuts import render

from main.models import Company


def view_home(request):
    home = Company.objects.all()
    return render(request, 'home.html', {'home': home})
