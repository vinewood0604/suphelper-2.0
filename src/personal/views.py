from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from account.models import Account, Theme

# Create your views here.
@login_required(login_url='login')
def home_screen_view(request):
	
	context = {}

	accounts = Account.objects.all()
	context['accounts'] = accounts

	if Theme.objects.filter(user=request.user.username).exists():
		color = Theme.objects.get(user=request.user.username).color
	else:
		color = 'white'

	return render(request, "personal/home.html", {'color': color})

@login_required(login_url='login')
def l2_tools_view(request):
	if Theme.objects.filter(user=request.user.username).exists():
		color = Theme.objects.get(user=request.user.username).color
	else:
		color = 'white'

	return render(request, 'personal/L2.html', {'color': color})

@login_required(login_url='login')
def openHistoryExtendedPage_view(request):
	if Theme.objects.filter(user=request.user.username).exists():
		color = Theme.objects.get(user=request.user.username).color
	else:
		color = 'white'

	return render(request, 'personal/openHistoryExtended.html', {'color': color})

@login_required(login_url='login')
def liveSearch_view(request):
	if Theme.objects.filter(user=request.user.username).exists():
		color = Theme.objects.get(user=request.user.username).color
	else:
		color = 'white'

	return render(request, 'personal/liveSearch.html', {'color': color})

@login_required(login_url='login')
def boAccountCreatePage_view(request):
	if Theme.objects.filter(user=request.user.username).exists():
		color = Theme.objects.get(user=request.user.username).color
	else:
		color = 'white'

	return render(request, 'personal/boAccountCreatePage.html', {'color': color})

@login_required(login_url='login')
def archiveRound_view(request):
	if Theme.objects.filter(user=request.user.username).exists():
		color = Theme.objects.get(user=request.user.username).color
	else:
		color = 'white'

	return render(request, 'personal/archiveRoundPage.html', {'color': color})

@login_required(login_url='login')
def archiveRedshiftRound_view(request):
	if Theme.objects.filter(user=request.user.username).exists():
		color = Theme.objects.get(user=request.user.username).color
	else:
		color = 'white'

	return render(request, 'personal/archiveRedshiftRoundPage.html', {'color': color})

@login_required(login_url='login')
def RTP_view(request):
	if Theme.objects.filter(user=request.user.username).exists():
		color = Theme.objects.get(user=request.user.username).color
	else:
		color = 'white'

	return render(request, 'personal/RTP.html', {'color': color})

@login_required(login_url='login')
def gameEnb_view(request):
	if Theme.objects.filter(user=request.user.username).exists():
		color = Theme.objects.get(user=request.user.username).color
	else:
		color = 'white'

	return render(request, 'personal/gameEnbPage.html', {'color': color})

@login_required(login_url='login')
def infoPage_view(request):
	if Theme.objects.filter(user=request.user.username).exists():
		color = Theme.objects.get(user=request.user.username).color
	else:
		color = 'white'

	return render(request, 'personal/infoPage.html', {'color': color})

@login_required(login_url='login')
def rtpCloning_view(request):
	if Theme.objects.filter(user=request.user.username).exists():
		color = Theme.objects.get(user=request.user.username).color
	else:
		color = 'white'

	return render(request, 'personal/rtpCloning.html', {'color': color})