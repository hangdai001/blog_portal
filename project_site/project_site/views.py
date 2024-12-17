from lib2to3.fixes.fix_input import context

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from app_site.models import Article, Categories, Image
from django.contrib.auth.models import User

from django.contrib.auth import  authenticate, login, logout
from random import shuffle



def AUTH_USER(request):
    if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        customer = User.objects.create_user(username, email, pass1)
        customer.first_name = first_name
        customer.last_name = last_name
        customer.save()
        return redirect('authentication')
    return render(request, 'registration/auth.html')

def HandleLogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('/admin/')
        else:
            return redirect('login')

    return render(request, 'registration/auth.html')

def HandleLogout(request):
    logout(request)
    return redirect('home')
    return render(request, 'main/home.html')

@login_required
def UserProfile(request):
    return render(request, 'registration/user_page.html')

def BASE(request):
    return render(request, 'main/base.html')

def HOME(request):
    articles = list(Article.objects.all())  # Convert queryset to list for shuffling
    shuffle(articles)  # randomize articles

    articles_latest = Article.objects.all().order_by('-created_date')  # Replace 'date' with your actual field name


    context = {
        'articles': articles,
        'articles_latest': articles_latest,
    }
    return render(request, 'main/home.html', context)

def CATA(request):
    articles = Article.objects.all()
    categories = Categories.objects.all()

    category_id = request.GET.get('category_id')
    if category_id:
        articles = Article.objects.filter(cat_id = category_id)
    else:
        articles = Article.objects.all()

    articles_first_batch = articles[:4]
    articles_second_batch = articles[4:6]

    context = {
        'articles': articles,
        'articles_first_batch': articles_first_batch,
        'articles_second_batch': articles_second_batch,
        'categories': categories,
    }
    return render(request, 'main/category.html', context)

def CONT(request):
    return render(request, 'main/contact.html')

def SINGLE(request, a_id):
    article = get_object_or_404(Article, a_id=a_id)
    return render(request, 'main/single.html', {'article': article})

def PHOTO(request):
    images = Image.objects.all()
    context = {
        'images': images,
    }
    return render(request, 'main/pgallery.html', context)