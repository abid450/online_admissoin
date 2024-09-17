from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class form_m(models.Model):
    Email = models.EmailField(max_length=200)
    Password = models.IntegerField()


class form_model(models.Model):
    username = models.CharField(max_length=200)
    email    = models.EmailField(max_length=200)
    phone  = models.CharField(max_length=150)
    rollnumber = models.CharField(max_length=150)
    regnumber  = models.CharField(max_length=150)
    Choise = models.CharField(max_length=150)

# Blog models -------------------------------------
class UserProfile(models.Model):
    Gendre_Choices = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    )
    Category = (
        ('Student', 'Student'),
        ('Teacher', 'Teacher'),
        ('Engineer', 'Engineer'),
        ('Doctor', 'Doctor'),
    )
    blood_group =(
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),

    )
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    Birth_Date = models.DateField()
    Blood_Group = models.CharField(max_length=3, choices=blood_group)
    Gender = models.CharField(max_length=50, choices=Gendre_Choices)
    Address = models.CharField(max_length=150)
    Phone = models.CharField(max_length=13)
    Nationality = models.CharField(max_length=30)
    Religion = models.CharField(max_length=50)
    Biodata = models.TextField()
    Profession = models.CharField(max_length=50, choices=Category)
    Image = models.ImageField(default='default.jpg', upload_to='login/images')

    def __str__(self):
        return f'{self.User.username} profile'
    def save(self):
        super().save()
        
