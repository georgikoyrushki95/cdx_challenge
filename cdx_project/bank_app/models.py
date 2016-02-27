from django.db import models
from django.contrib.auth.models import User

class EmergencyMessage(models.Model):
	user = models.ForeignKey(User)
	content = models.CharField(max_length = 500)

	def __unicode__(self):
		return self.content
