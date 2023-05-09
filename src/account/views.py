from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from account.forms import RegistrationForm, AccountAuthenticationForm, AccountUpdateForm
from account.models import Theme


def registration_view(request):
	context = {}
	if request.POST:
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			email = form.cleaned_data.get('email')
			raw_password = form.cleaned_data.get('password1')
			account = authenticate(email=email, password=raw_password)
			login(request, account)
			return redirect('home')
		else:
			context['registration_form'] = form
	else: # Otherwise expecting GET request.
		form = RegistrationForm()
		context['registration_form'] = form
	return render(request, 'account/register.html', context)

def logout_view(request):
	logout(request)
	return redirect("login")


def login_view(request):
	context = {}

	user = request.user
	if user.is_authenticated:
		return redirect("home")

	if request.POST:
		form = AccountAuthenticationForm(request.POST)
		if form.is_valid():
			email = request.POST['email']
			password = request.POST['password']
			user = authenticate(email=email, password=password)

			if user:
				login (request, user)
				return redirect("home")

	else:
		form = AccountAuthenticationForm()

	context['login_form'] = form
	return render(request, 'account/login.html', context)

def account_view(request):
	if not request.user.is_authenticated:
		return redirect("login")

	context = {}

	if request.POST:
		form = AccountUpdateForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			context['success_message'] = "Updated"
	else:
		form = AccountUpdateForm (
				initial = {
					"email": request.user.email,
					"username": request.user.username,
				}
			)
	context['account_form'] = form
	return render(request, 'account/account.html', context)

def theme_view(request):
	color = request.GET.get('color')

	if color == 'dark':
		if Theme.objects.filter(user=request.user.username).exists():
			user_theme = Theme.objects.get(user=request.user.username)
			user_theme.user = request.user.username
			user_theme.color = 'grey'
			user_theme.save()

		else:
			user2 = Theme(user=request.user.username, color='grey')
			user2.save()

	elif color == 'light':
		if Theme.objects.filter(user=request.user.username).exists():
			user_theme1 = Theme.objects.get(user=request.user.username)
			user_theme1.user = request.user.username
			user_theme1.color = 'white'
			user_theme1.save()

		else:
			user3 = Theme(user=request.user.username, color='white')
			user3.save()

	return redirect('/')