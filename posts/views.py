from django.shortcuts import render
from django.http import HttpResponseRedirect


def home(request):
    params = {
        'parm': 'Подарочные коробки'
    }
    return render(request, 'home.html', context=params)
