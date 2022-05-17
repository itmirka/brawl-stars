from django.shortcuts import render


def members(request):
	return render(request, 'members/members.html')