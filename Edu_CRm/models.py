from django.db import models
from django.contrib.auth.models import AbstractUser

class UserInfo(models.Model):  
    role = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, unique=True)
    address = models.TextField()
    date_of_birth = models.DateField()

    class Meta:
        abstract = True

class User(UserInfo):
    pass

class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    enrollment_date = models.DateField()

class Level(models.Model):
    name = models.CharField(max_length=255)

class Course(models.Model):
    name = models.CharField(max_length=255)

class Group(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    price = models.IntegerField()
    students = models.ManyToManyField(Student, related_name="groups")

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    status = models.BooleanField()
    date = models.DateField()

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    grade = models.CharField(max_length=10)
    date_assigned = models.DateField()

class Lead(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    status = models.CharField(max_length=255)
    date = models.DateField()

class CommunicationLog(models.Model):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True)
    message = models.TextField()
    date = models.DateField()

class Payment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    amount = models.BigIntegerField()
    date = models.DateField()
