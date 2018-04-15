from django.contrib import admin
from .models import Employee


class EmployeeModelAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('user', 'id_number')


admin.site.register(Employee, EmployeeModelAdmin)
