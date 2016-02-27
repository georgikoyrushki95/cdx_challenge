from django import forms
from bank_app.models import EmergencyMessage
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class EmergencyMessageForm(formst.ModelForm):
	content = forms.CharField(max_length = 500, help_text = "Please enter your emergency message")
	
	class Meta:
		model = EmergencyMessage