from django.contrib import admin
from employee.models import Employee, Department, Manager

admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(Manager)
