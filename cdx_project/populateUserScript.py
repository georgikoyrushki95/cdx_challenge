import string
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cdx_project.settings')
import django
django.setup()
from bank_app.models import UserProfile
from django.contrib.auth.models import User

f = open("team12.csv", 'r')
line = f.readline()[:-1]
for line in f:
    line = string.split(line, ',')
    name = line[1] + " " +  line[2]
    email = name + "@gmail.com"
    first_name = line[1]
    last_name = line[2]
    password = '123456'
    newUser = User(username = name, password = password, first_name = first_name,
                   last_name = last_name, email = email)

    newUser.save()
    newProfile = UserProfile(user = newUser, balance = 0.0)
    print newProfile.user.id
    newProfile.save()





# for line in f:
#     line = line[:len(line ) - 1]
#     line = string.split(line, ',')
#     #Attributes
#     name = line[1] + " " + line[2]
#
#     balance = float(line[3])
#     #Creating user
#     # newUser = User.objects.get_or_create(username = name, password = '123456',
#     #                email= name + "@gmail.com",
#     #                 first_name = line[1], last_name = line[2])
#     newUser = User(username = name, password = '123456',
#                    email= name + "@gmail.com",
#                    first_name = line[1], last_name = line[2])
#     userProfile = UserProfile()
#     newProfile = UserProfile.objects.get_or_create(user_profile = newUser, balance = 0.0)
#     newUser.save()
#     userProfile.balance = balance
#     userProfile.user_profile = newUser
#     print userProfile
#     userProfile.save()
