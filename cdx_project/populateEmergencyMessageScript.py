import random
import string
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cdx_project.settings')
import django
django.setup()
from bank_app.models import UserProfile, EmergencyMessage
from django.contrib.auth.models import User

f = open("emergency_messages.txt", 'r')

UserList = User.objects.all()
length = len(UserList)



for line in f:
    randomUser = UserList[random.randint(0, length - 1)]
    print randomUser
    newEmMessage= EmergencyMessage(user = randomUser, content=line)
    newEmMessage.save()
    
