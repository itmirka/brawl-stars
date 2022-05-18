from django.shortcuts import render


def club_wars(request):
	return render(request, 'club-wars/club-wars.html')
