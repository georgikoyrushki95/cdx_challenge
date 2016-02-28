from django import forms
from bank_app.models import EmergencyMessage, UserProfile
from django.contrib.auth.models import User

class UserProfileForm(forms.ModelForm):

    balance = forms.FloatField(initial= 0.0, widget = forms.HiddenInput())

    class Meta:
        model = UserProfile
        fields = ('balance', )

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class EmergencyMessageForm(forms.ModelForm):
	content = forms.CharField(max_length = 500, help_text = "Please enter your emergency message")
	class Meta:
		model = EmergencyMessage
        fields = ('content', )
