from django.shortcuts import render, redirect
from .forms import EmployeeForm, ProjectForm


def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_success')
    else:
        form = EmployeeForm()

    return render(request, 'add_employee.html', {'form': form})



#def add_project(request):
 #   if request.method == 'POST':
  #      form = ProjectForm(request.POST)
   #     if form.is_valid():
    #        form.save()
     #       return redirect('project_success')
    #else:
     #   form = ProjectForm()

    #return render(request, 'add_project.html', {'form': form})
