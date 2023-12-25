from django import forms

""" login form """
class login_form(forms.Form):
    username=forms.CharField(
        widget=forms.TextInput(),
        label='نام کاربری'
    )
    password=forms.CharField(
        widget=forms.TextInput(),
        label='پسورد'
    )