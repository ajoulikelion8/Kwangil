from django.shortcuts import render
from post.models import Post

# Create your views here.

def post_list(request):

    post_list = Post.objects.all()

    return render(request, 'post.html', {'post_list' : post_list})