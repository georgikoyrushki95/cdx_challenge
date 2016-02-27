from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from models import EmergencyMessage
from bank_app.forms import UserForm
from forms import EmergencyMessageForm
from django.contrib.auth import authenticate, login

def index(request):
	# messages = []
	# for m in EmergencyMessage.objects.all():
	# 	messages.append(m.content)
	print type(EmergencyMessage.objects.all())
	context_dict = {'messages' : EmergencyMessage.objects.all()}
	return render(request, 'bank_app/index.html', context_dict)


def register(request):
	registered = False

	if request.method == 'POST':
		user_form = UserForm(data = request.POST)

		if user_form.is_valid():
			user = user_form.save()

			user.set_password(user.password)
			user.save()
			registered = True
	else:
		user_form = UserForm()

	return render(request,
            'bank_app/register.html',
            {'user_form': user_form,  'registered': registered} )


def error_message(request):
	if request.method == 'POST':
		em_message_form = EmergencyMessageForm(data = request.POST)
		
		if em_message_form.isvalid() :
			emf = em_message_form.save()
			emf.user = request.user
			emf.save()
			return HttpResponseRedirect('/bank/')

	em_message_form = EmergencyMessageForm()
	context_dict = {'emergency_form' : em_message_form}
	return render(request, 'bank_app/error_message.html', context_dict)




def user_login(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

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

