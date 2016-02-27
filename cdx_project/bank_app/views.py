from django.shortcuts import render
from django.http import HttpResponse
from models import EmergencyMessage
from bank_app.forms import UserForm

def index(request):
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


def login(request):

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
		return render(request, 'bank/login.html', {})

