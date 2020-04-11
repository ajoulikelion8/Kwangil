from django.shortcuts import render
from myapp.models import Lion
from post.models import Post

# Create your views here.

def index(request):
    return render(request, 'index.html')

def lion_list(request):

    lion_list = Lion.objects.all()

    return render(request, 'lions.html', {'lion_list' : lion_list})

def post_list(request, pk):

    author = Lion.objects.get(pk = pk)
    post_list = Post.objects.all().filter(name = author)
    return render(request, 'lion_posts.html', {
        'post_list' : post_list,
        'author' : author
        })