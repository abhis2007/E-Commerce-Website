# from django import forms
# from .models import userProfileInfo
# from django.contrib.auth.models import User
#
# class userform(forms.ModelForm):
#     password=forms.CharField(widget=forms.PasswordInput())
#
#     class Meta():
#         model=User
#         fields=('username','first_name','last_name','email','password')
#
#
#     class userProfileInfoForm(forms.ModelForm):
#         class Meta():
#             model=userProfileInfo
#             fields=('picture')