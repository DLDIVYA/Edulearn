from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from thinkify.models import Exams


# class registerForm(forms.Form):
#     username = forms.CharField(max_length=200,widget=forms.EmailInput(attrs={'placeholder':"Enter you mail"}))
#     password = forms.CharField(max_length=200,widget=forms.PasswordInput(attrs={'placeholder':"Password"}))
#     confirm = forms.CharField(max_length=200,widget=forms.PasswordInput(attrs={'placeholder':"Confirm password"}))
#
#     def is_valid(self):
#         if self.password == self.confirm:
#             return True

class registerForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password']
        widgets = {'username': forms.TextInput(attrs={'placeholder': 'Username'}),
                   'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
                   'password': forms.PasswordInput(attrs={'placeholder': 'Password'})}


class UserLogin(AuthenticationForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))

class DomainFilter(forms.Form):
    domain = forms.CharField()

class ScholarFilter(forms.Form):
    Scholarship_exam = forms.CharField()

class Configure(forms.Form):
    choice_tup = ("Education","Central job","State job","College entrance")
    domain_type = forms.ChoiceField(choices=Exams.objects.all(), widget=forms.CheckboxInput)

