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

""" register form """
class register_form(forms.Form):
    Username=forms.CharField(
        widget=forms.TextInput(),
        label='نام کاربری'
    )
    email=forms.EmailField(
        widget=forms.EmailInput(),
        label='ایمیل'
    )
    first_name = forms.CharField(
        widget=forms.TextInput(),
        label='نام'
    )
    last_name = forms.CharField(
        widget=forms.TextInput(),
        label='نام خانوداگی'
    )
    Password=forms.CharField(
        widget=forms.PasswordInput(),
        label='پسورد'
    )
    Re_Password=forms.CharField(
        widget=forms.PasswordInput(),
        label='تکرار پسورد'
    )