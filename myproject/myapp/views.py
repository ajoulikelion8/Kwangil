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
    
    pk = pk
    author = Lion.objects.get(pk = pk)
    post_list = Post.objects.all().filter(name = author)
    
    return render(request, 'lion_posts.html', {
        'post_list' : post_list,
        'author' : author,
        'pk' : pk,
        })

def new_post(request, pk):
    
    author = Lion.objects.get(pk = pk)
    pk = pk

    if request.method == 'POST':    # POST 요청이면 form에 request된 값 저장
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)  #commit=False란 넘겨진 데이터를 바로 Post 모델에 저장하지는 말라는 뜻
            post.title = request.title
            post.content = request.content
            post.save()

            return redirect('lion_posts', pk = pk)     
    else:                           # GET 요청이면 그냥 form 보여줘
        form = PostForm()

    return render(request, 'new_post.html', {
        'form' : form,
        'author' : author,
        'pk' : pk,
        # 'post' : post,
        })