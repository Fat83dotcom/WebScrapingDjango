from datetime import datetime
from django.shortcuts import render
from .models import Portalcnn, Materiasportalcnn, Portalg1, Materiasportalg1
from .models import Portaluol, Materiasportaluol
from django.db import connection


def index(request):
    return render(request, 'Core/index.html', {
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
            'dadosAtualizacao': dadosAtualizacaoCnn,
        }
        return render(request, 'Core/noticiasCnn.html', contexto)


def coreG1(request):
    if request.method != 'GET':
        return render(request, 'Core/noticiasG1.html')
    else:
        dadosAtualizacaoG1 = Portalg1.objects.get(pk=0)
        consultaSQLPortalG1 = Portalg1.objects.all().order_by('id_pk')
        consultaSQLMateriasPortal = Materiasportalg1.objects.prefetch_related(
            'referencia_site').order_by('referencia_site_id')
        contexto = {
            'dadosPortal': consultaSQLPortalG1,
            'dadosMateria': consultaSQLMateriasPortal,
            'dadosAtualizacao': dadosAtualizacaoG1,
        }
        return render(request, 'Core/noticiasG1.html', contexto)


def coreUOL(request):
    if request.method != 'GET':
        return render(request, 'Core/noticiasUOL.html')
    else:
        dadosAtualizacaoUOL = Portaluol.objects.get(pk=0)
        consultaSQLPortalUOL = Portaluol.objects.all().order_by('id_pk')
        consultaSQLMateriasPortal = Materiasportaluol.objects.prefetch_related(
            'referencia_site').order_by('referencia_site_id')
        contexto = {
            'dadosPortal': consultaSQLPortalUOL,
            'dadosMateria': consultaSQLMateriasPortal,
            'dadosAtualizacao': dadosAtualizacaoUOL,
        }
        return render(request, 'Core/noticiasUOL.html', contexto)
