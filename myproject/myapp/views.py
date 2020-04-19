from django.shortcuts import render, redirect
from myapp.models import Lion
from post.models import Post
from .forms import PostForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def lion_list(request):

    lion_list = Lion.objects.all()

    return render(request, 'lions.html', {'lion_list' : lion_list})

def post_list(request, pk):
    
    post_pk = pk
    author = Lion.objects.get(pk = pk)
    lion_pk = author.pk

    post_list = Post.objects.all().filter(name = author)
    
    return render(request, 'lion_posts.html', {
        'post_list' : post_list,
        'author' : author,
        'post_pk' : post_pk,
        'lion_pk' : lion_pk,
        })

def new_post(request, pk):
    
    lion_pk = pk
    author = Lion.objects.get(pk = lion_pk)

    if request.method == 'POST':    # POST 요청이면 form에 request된 값 저장
        post = Post.objects.create(name = author)
        form = PostForm(request.POST, instance = post)

        if form.is_valid():
            post.save()

            return redirect('lion_posts', pk = lion_pk)     
    else:                           # GET 요청이면 그냥 form 보여줘
        form = PostForm()

    return render(request, 'new_post.html', {
        'form' : form,
        'author' : author,
        'lion_pk' :lion_pk,
        })