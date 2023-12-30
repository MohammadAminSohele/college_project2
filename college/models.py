from django.db import models

from django.db.models import Q

# Create your models here.

class Teacher(models.Model):
    nat_code = models.CharField(max_length = 150)
    first_name = models.CharField(max_length = 150)
    last_name = models.CharField(max_length = 150)
    birthday_date = models.DateField()
    telephone = models.CharField(max_length = 150)
    mobile = models.CharField(max_length = 150)
    email = models.EmailField()
    field = models.CharField(max_length = 150)
    regdate = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f'{self.first_name}-{self.last_name}'


class product_manager(models.Manager):
    def search(self, query):
        lookup = (
            Q(nat_code__icontains=query) 
        )
        return self.get_queryset().filter(lookup).distinct()
    def get_by_id(self, studentId):
        qs = self.get_queryset().filter(id=studentId)
        if qs.count() == 1:
            return qs.first()
        return None

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

    objects=product_manager()

    def __str__(self):
        return f'{self.first_name}-{self.last_name}'
class Level(models.Model):
    name = models.CharField(max_length = 150,null=True)
    regdate = models.DateField(null=True)
    description = models.TextField()

    def __str__(self):
        return self.name
class Course(models.Model):
    name = models.CharField(max_length = 150)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    regdate = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.name
class Term(models.Model):
    name = models.CharField(max_length = 150)
    startDate = models.DateField()
    endDate = models.DateField()
    regdate = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.name
    
class StudentTerm(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    term = models.ForeignKey(Term, on_delete=models.CASCADE)
    regdate = models.DateField()
    description = models.TextField()
    

    def __str__(self):
        return self.student.last_name 


class TeacherTerm(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    term = models.ForeignKey(Term, on_delete=models.CASCADE)
    regdate = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f'{self.teacher.first_name}-{self.teacher.last_name}'