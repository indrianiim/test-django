from django import forms
from django.shortcuts import redirect, render
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . forms import CreateArticle

# Create your views here.

def index (request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/index.html', {'articles':articles })

def detail(request, slug):
    # return HttpResponse(slug)
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/detail.html', {'article':article })

@login_required(login_url="/accounts/login/")
def create(request):
    if request.method == 'POST':
        form = CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            #save article to db
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('articles:list')
    else:       
        form = CreateArticle()
    return render(request, 'articles/create.html', {'form': form})