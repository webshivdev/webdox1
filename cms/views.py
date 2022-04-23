from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from cms.models import Post
from cms.forms import PostForm
# Create your views here.

def home(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request, "cms/index.html", context)

def about(request):
    return render(request, "cms/about.html")

def product(request):
    return render(request, "cms/products.html")

def enquiry(request):
    return render(request, "cms/enquiry.html")

def help(request):
    return render(request, "cms/help.html")

def single(request, pk):
    post = Post.objects.get(pk=pk)
    context = {'post':post}
    return render(request, "cms/single.html", context)

@login_required
def create_post(request):
    form = PostForm()
    context = {'form': form}
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('single', pk=post.pk)
    return render(request, 'cms/create_post.html', context)

