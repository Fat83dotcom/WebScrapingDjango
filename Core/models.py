# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Materiasportal(models.Model):
    id_pk = models.IntegerField(primary_key=True)
    referencia_site = models.ForeignKey('Portalcnn', models.DO_NOTHING, db_column='referencia_site', blank=True, null=True)
    dt_materia = models.DateField(blank=True, null=True)
    link_materia = models.TextField(blank=True, null=True)
    titulo_materia = models.TextField(blank=True, null=True)
    texto_materia = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'materiasportal'


class Portalcnn(models.Model):
    id_pk = models.IntegerField(primary_key=True)
    dt_hr_pesquisa = models.DateTimeField(blank=True, null=True)
    nome_sessao = models.CharField(max_length=100, blank=True, null=True)
    link_site = models.CharField(unique=True, max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'portalcnn'


class LogServicos(models.Model):
    dt_hr_exec_func = models.DateTimeField(null= True)