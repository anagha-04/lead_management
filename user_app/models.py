from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class StudentLeadModel(models.Model):

      SOURCE_CHOICES = [
        ("FRIEND","friend"),
        ("INSTAGRAM","instagram"),
        ("OWN","own")
    
      ]
      student_name= models.CharField(max_length=50)

      Qualification = models.CharField(max_length=50)

      phone_number = models.IntegerField(max_length=12)

      user = models.ForeignKey(User,on_delete=models.CASCADE)

      source =models.CharField(max_length=30,choices=SOURCE_CHOICES)

      created_date = models.DateField(auto_now_add=True)
