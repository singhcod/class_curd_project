from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)


    def __str__(self):
        return self.name
#
# class Student(models.Model):
#     student_id = models.AutoField()
#     name = models.CharField(max_length=100)
#     roll = models.IntegerField()
#     class_name = models.CharField(max_length=100)
#     address = models.CharField(max_length=200)
#
#     def __str__(self):
#         return self.name
