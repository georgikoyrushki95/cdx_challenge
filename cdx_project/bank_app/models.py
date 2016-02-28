from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	balance = models.FloatField(default=0.0)

	def __unicode__(self):
		return self.user

class EmergencyMessage(models.Model):
	user = models.ForeignKey(User)
	content = models.TextField(max_length = 1000)

	def __unicode__(self):
		return self.content
