from django.shortcuts import render


def index(request):
    return render(request, 'Core/index.html')


def coreCnn(request):
    return render(request, 'Core/noticiasCnn.html')
