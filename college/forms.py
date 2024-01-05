from django import forms

from .import models

class StudentForm(forms.ModelForm):
    class Meta:
        model = models.Student
        fields = '__all__'


class TeacherForm(forms.ModelForm):
    class Meta:
        model = models.Teacher
        fields = '__all__'

class StudentTermForm(forms.ModelForm):
    class Meta:
        model = models.StudentTerm
        fields = '__all__'

class StudentPaymentForm(forms.ModelForm):
    class Meta:
        model = models.Payment
        fields = 'student','date_of_payment','price','code'

class TeacherTermForm(forms.ModelForm):
    class Meta:
        model = models.TeacherTerm
        fields = '__all__'