from django.db import models

class AccountUser(models.Model):
    username=models.CharField(max_length=50)
    Email=models.EmailField()
    address=models.CharField(max_length=100)

    def __str__(self):
        return str(self.id)+" "+self.Email
