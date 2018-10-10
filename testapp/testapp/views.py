from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def home(request):
	print(dir(request.user))
	return render(request, 'testapp/home.html')