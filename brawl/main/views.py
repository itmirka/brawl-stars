from django.shortcuts import render


def index(request):
	return render(request, 'main/index.html')

def members(request):
	return render(request, 'main/members.html')
