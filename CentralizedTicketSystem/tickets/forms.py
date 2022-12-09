from django.forms import ModelForm

from CentralizedTicketSystem.tickets.models import Employee, Department, Task, Comment


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'department']


class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = ['name']


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['employee', 'description', 'completed', 'departments', 'due_date', 'urgency']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['task', 'employee', 'comment']