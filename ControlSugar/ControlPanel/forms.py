from django import forms

class loginForm(forms.Form):
    login = forms.TextInput()
    password = forms.TextInput()

class loginForm(forms.Form):
    Name = forms.CharField() # Имя пользователя 
    Surname = forms.CharField() # Фамилия 
    age = forms.DateField()
    Password = forms.CharField()
    twoPassword = forms.CharField()
    Login = forms.CharField()