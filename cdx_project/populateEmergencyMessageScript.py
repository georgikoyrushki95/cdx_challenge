import random
import string
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cdx_project.settings')
import django
django.setup()
from bank_app.models import UserProfile, EmergencyMessage

f = open("emergency_messages.txt", 'r')

UserProfileList = UserProfile.objects.all()
length = len(UserProfileList)



for line in f:
    randomUserProfile = UserProfileList[random.randint(0, length - 1)]
    newEmMessage = EmergencyMessage(user_profile = randomUserProfile, content = line)
    newEmMessage.save()
    
