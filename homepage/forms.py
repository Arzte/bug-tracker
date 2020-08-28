from django import forms

from myuser.models import MyUser


class LoginForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['username', 'password',
                  'first_name', 'last_name', 'password']
