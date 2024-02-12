from employee.views import list_employees, add_employees, delete_employees
from django.urls import path

urlpatterns = [
    path('list/', list_employees, name='employee_list'),
    path('add/', add_employees, name='employee_add'),
    path('delete/<int:employee_id>/', delete_employees, name='employee_delete')
]
