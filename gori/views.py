from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import History, Culture, Architect, AboutProjectDonors

#for index page
def index_wout_lang(request)
	return render(request, 'index.html')

def index_page(request, lang):
	aboutproject = AboutProjectDonors.objects.last()
	allposthistory = History.objects.all()
	allpostculture = Culture.objects.all()

	all_post_history = []
	for i in allposthistory:
		all_post_history.insert(0, i)

	all_post_culture = []
	for i in allpostculture:
		all_post_culture.insert(0, i)

	last_post_history = all_post_history[0]
	lastsec_post_history = all_post_history[1]

	last_post_culture = all_post_culture[0]
	lastsec_post_culture = all_post_culture[1]

	return render(request, 'index.html', {'lang':lang, 
		'last_post_history':last_post_history, 
		'lastsec_post_history':lastsec_post_history,
		'last_post_culture':last_post_culture,
		'lastsec_post_culture':lastsec_post_culture,
		'about_project':aboutproject,})


#for about page
def about_project(request, lang):
	aboutproject = AboutProjectDonors.objects.last()
	return render(request, 'aboutproject.html', {'lang':lang, 'about_project':aboutproject})


#for history page
def history(request, lang):
	allpost = History.objects.all()
	all_post = []
	for i in allpost:
		all_post.insert(0, i)

	return render(request, 'history.html', {'lang':lang, 'posts':all_post})


#for culture page
def culture(request, lang):
	allpost = Culture.objects.all()
	
	all_post = []
	for i in allpost:
		all_post.insert(0, i)

	return render(request, 'culture.html', {'lang':lang, 'posts':all_post})


#for architect page
def architect(request, lang):
	allpost = Architect.objects.all()
	
	all_post = []
	for i in allpost:
		all_post.insert(0, i)

	return render(request, 'architect.html', {'lang':lang, 'posts':all_post})
