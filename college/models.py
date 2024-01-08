from django.db import models

from django.db.models import Q

# Create your models here.


    
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

class Teacher(models.Model):
    nat_code = models.CharField(max_length = 150,verbose_name='کد ملی استاد')
    first_name = models.CharField(max_length = 150,verbose_name='نام استاد')
    last_name = models.CharField(max_length = 150,verbose_name='نام خانوادگی استاد')
    birthday_date = models.DateField(verbose_name='تاریخ تولد استاد')
    telephone = models.CharField(max_length = 150,verbose_name='شماره تلفن ثابت استاد')
    mobile = models.CharField(max_length = 150,verbose_name='شماره تلفن استاد')
    email = models.EmailField(verbose_name='ایمیل استاد')
    field = models.CharField(max_length = 150,verbose_name='رشته تحصیلی استاد')
    regdate = models.DateField(verbose_name='تاریخ ثبت استاد')
    description = models.TextField(verbose_name='توضیحات')

    objects=product_manager()

    def __str__(self):
        return f'{self.first_name}-{self.last_name}'

class Student(models.Model):
    nat_code = models.CharField(max_length = 150,verbose_name='کد ملی')
    first_name = models.CharField(max_length = 150,verbose_name='نام دانشجو')
    last_name = models.CharField(max_length = 150,verbose_name='نام خانوادگی دانشجو')
    birthday_date = models.DateField(verbose_name='تاریخ تولد دانشجو')
    telephone = models.CharField(max_length = 150,verbose_name='شماره تلفن ثابت دانشجو')
    mobile = models.CharField(max_length = 150,verbose_name='شماره تلفن همراه دانشجو')
    email = models.EmailField(verbose_name='ایمیل دانشجو')
    score = models.IntegerField(verbose_name='نمره دانشجو')
    regdate = models.DateField(verbose_name='تاریخ ثبت دانشجو')
    description = models.TextField(verbose_name='توضیحات')
    # payment = models.ForeignKey(Payment, on_delete=models.CASCADE,null=True)
    

    objects=product_manager()

    # college/show/student/3

    def __str__(self):
        return f'{self.first_name}-{self.last_name}'
    
class Payment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE,null=True,verbose_name='دانشجو')
    date_of_payment = models.DateField(verbose_name='تاریخ پرداخت')
    total = models.IntegerField(default=2000000,blank=True,null=True,verbose_name='مبلغ قابل پرداختت')
    price = models.IntegerField(verbose_name='مبلغ')
    account = models.CharField(max_length = 150,default=6037991784183869,verbose_name='به حساب')
    remaining_price = models.CharField(max_length = 150,null=True,blank=True,verbose_name='مبلغ مانده')
    code = models.CharField(max_length = 150,null=True,verbose_name='کد پیگیری')

    objects=product_manager()
    
    def __str__(self):
        return self.student.first_name

class TeacherPayment(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE,null=True,verbose_name='استاد')
    date_of_payment = models.DateField(verbose_name='تاریخ پرداخت')
    hours = models.IntegerField(verbose_name='ساعت')
    price_in_hour=models.IntegerField(verbose_name='حقوق ساعت')
    total=models.IntegerField(verbose_name='مجموع',blank=True,null=True)
    account = models.CharField(max_length = 150,default=6037991784183869,verbose_name='به حساب')

    def __str__(self):
        return f'{self.teacher.first_name}-{self.teacher.last_name}'

    objects=product_manager()

class Level(models.Model):
    name = models.CharField(max_length = 150,null=True,verbose_name='نام مقطع')
    regdate = models.DateField(null=True,verbose_name='تاریخ ثبت')
    description = models.TextField(verbose_name='توضیحات')

    def __str__(self):
        return self.name
class Course(models.Model):
    name = models.CharField(max_length = 150,verbose_name='نام درس')
    level = models.ForeignKey(Level, on_delete=models.CASCADE,verbose_name='مقطع')
    regdate = models.DateField(verbose_name='تاریخ ثبت')
    description = models.TextField(verbose_name='توضیحات')

    def __str__(self):
        return self.name
class Term(models.Model):
    name = models.CharField(max_length = 150,verbose_name='نام ترم')
    startDate = models.DateField(verbose_name='تاریخ شروع')
    endDate = models.DateField(verbose_name='تاریخ پایان')
    regdate = models.DateField(verbose_name='تاریخ ثبت')
    description = models.TextField(verbose_name='توضیحات')

    def __str__(self):
        return self.name
    
class StudentTerm(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE,verbose_name='دانشجو')
    course = models.ForeignKey(Course, on_delete=models.CASCADE,verbose_name='درس')
    term = models.ForeignKey(Term, on_delete=models.CASCADE,verbose_name='ترم')
    regdate = models.DateField(verbose_name='تاریخ ثبت')
    description = models.TextField(verbose_name='توضیحات')
    
    objects=product_manager()

    def __str__(self):
        return self.student.last_name 
    

class TeacherTerm(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE,verbose_name='استاد')
    course = models.ForeignKey(Course, on_delete=models.CASCADE,verbose_name='درس')
    term = models.ForeignKey(Term, on_delete=models.CASCADE,verbose_name='ترم')
    regdate = models.DateField(verbose_name='تاریخ ثبت')
    class_number = models.IntegerField(null=True,verbose_name='شماره کلاس')
    description = models.TextField(verbose_name='توضیحات')

    def __str__(self):
        return f'{self.teacher.first_name}-{self.teacher.last_name}'