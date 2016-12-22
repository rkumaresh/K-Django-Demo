from django import forms


class LoginForm(forms.Form):
    inputData = forms.CharField(label="userName")

class ToDoForm(forms.Form):
    userName = forms.CharField(label="userName", widget=forms.HiddenInput)
    surveyId = forms.CharField(label="surveyId")
