from django.shortcuts import render, HttpResponse, redirect, reverse
from employee.models import Employee, Department, Manager
from employee.forms import EmployeeForm


def list_managers(request):
    managers = Manager.objects.all()
    return HttpResponse(managers, safe=False)


def list_employees(request):
    employees = Employee.objects.all()
    return render(request, 'list.html', {
        'objects': employees
    })


def delete_employees(request, employee_id):
    a = Employee.objects.get(id=employee_id)
    a.delete()
    return redirect(reverse('list_employees'))


def add_employees(request):
    if request.method == 'GET':
        form = EmployeeForm()
        return render(request, 'add.html', {'form': form})
    elif request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list.html')
