from django.contrib import admin
from .models import LogServicos


class LogServicosAdmin(admin.ModelAdmin):
    list_display = ['id', 'dt_hr_exec_func', 'func_portal']


admin.site.register(LogServicos, LogServicosAdmin)
