from datetime import datetime
from django.shortcuts import render
from .models import Materiasportal, Portalcnn
from django.db import connection

def index(request):
    consultaSQL = Portalcnn.objects.get(pk=0)
    return render(request, 'Core/index.html', {
        'dtAtualizacao': consultaSQL,
    })


# def consultaPortaCnn():
#     with connection.cursor() as cursor:
#         sql = 

def coreCnn(request):
    if request.method != 'GET':
        return render(request, 'Core/noticiasCnn.html')
    else:
        consultaSQL = Portalcnn.objects.prefetch_related('referencia_site')
        # print(consultaSQL.get(referencia_site_id=0))
        contexto = {
            'dados': consultaSQL,
        }
        return render(request, 'Core/noticiasCnn.html', contexto)