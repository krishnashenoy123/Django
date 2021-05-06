from django.shortcuts import render

posts = [
    {
        'author': 'krishna',
        'date': '5 May 2021',
        'content': 'Blog post 1',
        'title': 'djangappa',
    },
    {
        'author': 'akshaj',
        'date': '21 May 2021',
        'title': 'super daily',
        'content': 'Blog post 2',
    }
]

# Create your views here.
def home(request):
    context = {
        'data': posts
    }
    return render(request, 'mave/home.html', context)

def about(request):
    return render(request, 'mave/about.html', {'title': 'About'})

