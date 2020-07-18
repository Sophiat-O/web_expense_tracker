from django.db import models

# Create your models here.

class Users(models.Model):
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=16)
    date_created = models.DateTimeField('Date Created')

class Log(models.Model):
    userid = models.ForeignKey(Users, on_delete=models.CASCADE)
    login_date = models.DateTimeField

class Expenses(models.Model):
    userid = models.ForeignKey(Users, on_delete=models.CASCADE)
    income_expense = models.CharField(max_length=20)
    category = models.CharField(max_length=100)
    amount = models.IntegerField
    expense_date = models.DateTimeField
