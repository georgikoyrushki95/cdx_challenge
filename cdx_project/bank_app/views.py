from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from models import EmergencyMessage, UserProfile
from bank_app.forms import UserForm, UserProfileForm, EmergencyMessageForm
from forms import EmergencyMessageForm
from django.contrib.auth import authenticate, login, logout
from django.utils.html import escape
def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/bank/')


def index(request):
	if request.method == "POST":
		message = EmergencyMessage(content = escape(request.POST.get('content')),  user = request.user)
		message.save()

	message_form = EmergencyMessageForm()
	if (request.user.id):
		user = request.user
		userProfile = UserProfile.objects.get(user = user)
		context_dict = {'messages' : EmergencyMessage.objects.all()[::-1], 'message_form': message_form, 'user_profile': userProfile}
	else:
		context_dict = {'messages' : EmergencyMessage.objects.all()[::-1], 'message_form': message_form}
	return render(request, 'bank_app/index.html', context_dict)


def register(request):
	registered = False

	if request.method == 'POST':
		user_form = UserForm(data = request.POST)
		user_profile_form = UserProfileForm(data = request.POST)
		#print user_form.is_valid()
		if user_form.is_valid() and user_profile_form.is_valid():
			print "Hello"
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			user_profile = user_profile_form.save(commit = False)
			user_profile.user = user
			user_profile.save()
			registered = True
		else:
			print "Hello"
	else:
		user_profile_form = UserProfileForm()
		user_form = UserForm()

	return render(request,
            'bank_app/register.html',
            {'user_form': user_form,  'registered': registered, 'user_profile_form': user_profile_form})


def emergency_message(request):
	if request.method == 'POST':
		em_message_form = EmergencyMessageForm(data = request.POST)
		
		if em_message_form.isvalid() :
			emf = em_message_form.save()
			emf.user = request.user
			emf.save()
			return HttpResponseRedirect('/bank/')

	em_message_form = EmergencyMessageForm()
	context_dict = {'emergency_form' : em_message_form}
	return render(request, 'bank_app/emergency_message.html', context_dict)




def user_login(request):

	if request.method == 'POST':
		username = escape(request.POST.get('username'))
		password = escape(request.POST.get('password'))

		user = authenticate(username = username, 
			password = password)

		if user:

			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/bank/')
			else:

				return HttpResponse("Your account is disabled")

		else:
			return HttpResponse("Invalid login details supplied")

	else:
		return render(request, 'bank_app/login.html', {})

