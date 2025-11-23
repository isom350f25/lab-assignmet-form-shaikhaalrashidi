from django.urls import path
from django.shortcuts import render
from . import views

urlpatterns = [
    path('add-employee/', views.add_employee, name='add_employee'),
    path('add-project/', views.add_project, name='add_project'),

    path('employee-success/', lambda request: render(request, 'success.html', {'msg': 'Employee added!'}), name='employee_success'),
    path('project-success/', lambda request: render(request, 'success.html', {'msg': 'Project added!'}), name='project_success'),
]