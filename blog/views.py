from django.shortcuts import render


# Create your views here.

posts = [
	{
		'author': 'Harsha',
		'title': 'Blog Post 1',
		'content': 'First post content',
		'date_posted': 'Jan 14, 2019'
	},
	{
		'author': 'PavanKumar',
		'title': 'Blog Post 2',
		'content': 'second post content',
		'date_posted': 'Jan 15, 2019'
	}
		
]


def home(request):
	context = {
		'posts': posts
	}
	return render(request, 'blog/home.html', context)
	
def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})