from django.shortcuts import render


def index(request):
    return render(request, 'importing/index.html')


def importar(request):
    return render(request, 'importing/importar.html')
