from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect

@login_required
def home(request):
	print(dir(request.user))
	return render(request, 'testapp/home.html')


def logout_view(request):
	logout(request)
	return redirect('/')