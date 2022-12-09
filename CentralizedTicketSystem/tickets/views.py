from django.shortcuts import render

from CentralizedTicketSystem.tickets.forms import EmployeeForm, DepartmentForm, TaskForm, CommentForm
from CentralizedTicketSystem.tickets.models import Employee, Department, Task, Comment


def all_data(request):
    # Get all the employees, departments, tasks, and comments
    employees = Employee.objects.all()
    departments = Department.objects.all()
    tasks = Task.objects.all()
    comments = Comment.objects.all()

    # Create the forms
    employee_form = EmployeeForm()
    department_form = DepartmentForm()
    task_form = TaskForm()
    comment_form = CommentForm()
    context = {
        'employees': employees,
        'departments': departments,
        'tasks': tasks,
        'comments': comments,
        'employee_form': employee_form,
        'department_form': department_form,
        'task_form': task_form,
        'comment_form': comment_form,
    }
    # Render the template
    return render(request, 'data.html', context)
