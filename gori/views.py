from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import History, Culture, Architect, AboutProjectDonors, Human, Video

#for index page
def index_wout_lang(request):
	response = redirect('ka/')
	return response

def index_page(request, lang):
	firstvideo = Video.objects.get(id = 1)
	secondvideo = Video.objects.get(id = 2)
	thirdsvideo = Video.objects.get(id = 3)
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
		'about_project':aboutproject,
		'firstvideo':firstvideo,
		'secondvideo':secondvideo,
		'thirdsvideo':thirdsvideo})


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

def history_detail_view(request, id, lang):
    try:
        history = History.objects.get(id=id)
    except History.DoesNotExist:
        raise Http404('Post does not exist')

    return render(request, 'history_detail.html', context={'lang':lang, 'history': history})



#for culture page
def culture(request, lang):
	allpost = Culture.objects.all()
	
	all_post = []
	for i in allpost:
		all_post.insert(0, i)

	return render(request, 'culture.html', {'lang':lang, 'posts':all_post})

def culture_detail_view(request, id, lang):
    try:
        history = Culture.objects.get(id=id)
    except History.DoesNotExist:
        raise Http404('Post does not exist')

    return render(request, 'culture_detail.html', context={'lang':lang, 'history': history})


#for architect page
def architect(request, lang):
	allpost = Architect.objects.all()
	
	all_post = []
	for i in allpost:
		all_post.insert(0, i)

	return render(request, 'architect.html', {'lang':lang, 'posts':all_post})

def architect_detail_view(request, lang, id):
    try:
        history = Architect.objects.get(id=id)
    except History.DoesNotExist:
        raise Http404('Post does not exist')

    return render(request, 'architect_detail.html', context={'lang':lang, 'history': history})


#search page
def search(request, lang):
	try:
		search_text = request.GET["search_text"]

	except:
		search_text = 'გორი'

	history = History.objects.all()
	culture = Culture.objects.all()
	architect = Architect.objects.all()
	searched_posts = []
	if lang == 'ka':
		for i in history:
			if (search_text in i.post_text.text_ka) or (search_text in i.post_title.text_ka):
				searched_posts.append(i)

		for i in culture:
			if (search_text in i.post_text.text_ka) or (search_text in i.post_title.text_ka):
				searched_posts.append(i)

		for i in architect:
			if (search_text in i.post_text.text_ka) or (search_text in i.post_title.text_ka):
				searched_posts.append(i)

	if lang == 'en':
		for i in history:
			if (search_text in i.post_text.text_en) or (search_text in i.post_title.text_en):
				searched_posts.append(i)

		for i in culture:
			if (search_text in i.post_text.text_en) or (search_text in i.post_title.text_en):
				searched_posts.append(i)

		for i in architect:
			if (search_text in i.post_text.text_en) or (search_text in i.post_title.text_en):
				searched_posts.append(i)



	return render(request, 'search.html', {'lang':lang, 'search_text':search_text, 'searched_posts':searched_posts})

# def search_no(request, lang):
# 	print(request.GET["search_text"])
# 	search_text = search
# 	history = History.objects.all()
# 	culture = Culture.objects.all()
# 	architect = Architect.objects.all()
# 	searched_posts = []

# 	for i in history:
# 		searched_posts.append(i)

# 	for i in culture:
# 		searched_posts.append(i)

# 	for i in architect:
# 		searched_posts.append(i)
# 	print(searched_posts)

# 	return render(request, 'search.html', {'lang':lang, 'searched_posts':searched_posts})


#text us page

def text_us(request, lang):
	if request.method == 'POST':
		print(request.POST)
	return render(request, 'textus.html', {'lang':lang})


#humans page
def humans(request, lang):
	allpost = Human.objects.all()
	all_post = []
	for i in allpost:
		all_post.insert(0, i)
	return render(request, 'humans.html', {'lang':lang, 'humans':all_post})


def humans_detail(request, lang, id):
	allpost = Human.objects.all()
	all_post = []
	for i in allpost:
		if i.id == id:
			continue
			
		all_post.insert(0, i)

	try:
		human = Human.objects.get(id=id)
	except History.DoesNotExist:
		raise Http404('Post does not exist')

	return render(request, 'humans_detail.html', context={'lang':lang, 'human': human,'humans':all_post})


#videos page
def videos(request, lang):
	allpost = Video.objects.all()
	
	all_post = []
	for i in allpost:
		all_post.insert(0, i)
	return render(request, 'videos.html', {'lang':lang, 'videos':all_post})