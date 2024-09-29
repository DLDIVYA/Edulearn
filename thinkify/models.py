from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Thinkis(models.Model):
    username = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    persona = models.CharField(max_length=200, null=True)


class Exams(models.Model):
    domain = models.CharField(max_length=200, null=True)
    examname = models.CharField(max_length=200, null=True)
    link = models.CharField(max_length=200, null=True)
    eligibility = models.CharField(max_length=200, null=True)
    exam_date = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.examname

class Scholarship(models.Model):
    Scholarship_exam = models.CharField(max_length=200, null=True)
    link = models.CharField(max_length=200, null=True)
    eligibility = models.CharField(max_length=200, null=True)
    examdate = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.Scholarship_exam

class Resources(models.Model):
    Exam_name = models.CharField(max_length=200, null=True)
    link = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.Exam_name


class persdomain(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    domain_name = models.CharField(max_length=200,null=True)