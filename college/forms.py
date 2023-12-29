from django import forms

from .import models

class StudentForm(forms.ModelForm):
    class Meta:
        model = models.Student
        fields = '__all__'


class StudentTermForm(forms.ModelForm):
    class Meta:
        model = models.StudentTerm
        fields = '__all__'