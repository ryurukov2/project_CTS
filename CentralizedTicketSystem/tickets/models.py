from django.db import models
from django.forms import ModelForm


class Department(models.Model):
    name = models.CharField(max_length=100)


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.RESTRICT)


class Task(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    completed = models.BooleanField()
    departments = models.ManyToManyField(Department)
    due_date = models.DateField()
    urgency = models.CharField(max_length=10, choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')])


class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.SET_DEFAULT, default="[deleted]")
    comment = models.TextField()



