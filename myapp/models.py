from django.db import models

# Create your models here.
#Company table
class Company(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return (str(self.name))

#Profile table
class Profile(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    #company foreign key
    #on deleting the company the profile linking to it will also be delete
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return (str(self.name))

