from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Employee
from django.http.response import HttpResponse
from django.shortcuts import redirect


def base_view(request):
    return render(request, 'html/sub1.html')


def employee_created(request):
    return render(request, 'employee/create.html')


def employee_updated(request):
    return render(request, 'employee/update.html')


def main_page(request):
    return render(request, 'employee/main.html')


def update_info(request):
    return render(request, 'employee/update_employee_info.html')


def update_employee(request):
    if request.method == 'POST':
        pk = request.POST.get('employee_id')
        context = {'message': 'Employee id is required'}
        if pk:
            employee_object = Employee.objects.filter(id=pk)
            if employee_object:
                return redirect('update-employee', pk=pk)
            context = {'message': 'Employee does not exist', 'id': pk}
        return render(request, 'employee/update_employee_info.html', context=context)
