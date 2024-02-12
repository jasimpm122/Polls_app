from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class Manager(models.Model):
    name = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Employee(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )

    name = models.CharField(max_length=64)
    DOB = models.DateField()
    email = models.EmailField()
    mobile_number = models.TextField()
    manager = models.ForeignKey(Manager, on_delete=models.PROTECT)
    designation = models.CharField(max_length=100, blank=True, null=True)
    marital_status = models.CharField(blank=True, null=True, max_length=100)
    age = models.SmallIntegerField()
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1)
    address = models.TextField(blank=True, null=True)
    doj = models.DateField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
