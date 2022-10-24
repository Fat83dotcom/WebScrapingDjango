from datetime import datetime
from django.shortcuts import render
from .models import Materiasportalcnn, Portalcnn
from django.db import connection


def index(request):
    consultaSQL = Portalcnn.objects.get(pk=0)
    return render(request, 'Core/index.html', {
        'dtAtualizacao': consultaSQL,
    })


def coreCnn(request):
    if request.method != 'GET':
        return render(request, 'Core/noticiasCnn.html')
    else:
        dadosAtualizacaoCnn = Portalcnn.objects.get(pk=0)
        consultaSQLPortalCnn = Portalcnn.objects.all()
        consultaSQLMateriasPortal = Materiasportalcnn.objects.prefetch_related(
            'referencia_site').order_by('referencia_site_id')
        contexto = {
            'dadosPortal': consultaSQLPortalCnn,
            'dadosMateria': consultaSQLMateriasPortal,
            'dadosAtualizacao': dadosAtualizacaoCnn
        }
        return render(request, 'Core/noticiasCnn.html', contexto)
