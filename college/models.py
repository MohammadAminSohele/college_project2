from django.db import models

# Create your models here.

class Student(models.Model):
    nat_code = models.CharField(max_length = 150)
    first_name = models.CharField(max_length = 150)
    last_name = models.CharField(max_length = 150)
    birthday_date = models.DateField()
    telephone = models.CharField(max_length = 150)
    mobile = models.CharField(max_length = 150)
    email = models.EmailField()
    score = models.IntegerField()
    regdate = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f'{self.first_name}-{self.last_name}'