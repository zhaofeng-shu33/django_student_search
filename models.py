from django.db import models

# Create your models here.
class Student(models.Model):
    student_id = models.CharField(max_length=13, primary_key = True)
    student_name = models.CharField(max_length=3)
    student_dormitory = models.CharField(max_length=6)
    student_gender = models.CharField(max_length=1, choices=(('M','Male'),('F', 'Female')), default='M')
    def __str__(self):
        return "({0},{1})".format(self.student_name,self.student_id)