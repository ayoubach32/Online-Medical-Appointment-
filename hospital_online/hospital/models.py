from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    date_of_birth = models.DateField( null=True)

    def __str__(self):
        return self.user.username

class Doctor (models.Model):
    name = models.CharField(max_length=40)

    def __str__(self) :
        return self.name
    
class Appointment(models.Model):
    user = models.ForeignKey(Profile , on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor , on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self) :
          return f"Appointment with {self.doctor} on {self.date} at {self.time}"
    
    
