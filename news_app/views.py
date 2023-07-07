from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from .models import News
from haystack.generic_views import SearchView

# Create your views here.


def home(request):
    message = request.GET.get('message')
    data = News.objects.all()
    context ={
        'year':timezone.now().year,
        'data': data,
        'user': request.user,
        'message': message
    }
    return render(request, 'news/index.html', context)



def details(request, id):
    news = News.objects.filter(id=id).first()
    context = {
                'by': news.by, 
                'descendants': news.descendants, 
                'id': news.id, 
                'kids': news.kids, 
                'score': news.score, 
                'text': news.text, 
                'title': news.title,
                'type': news.news_type,
                'is_hacker_news': news.is_hacker_news,
                'time': news.time
                }

    return render(request, 'news/details.html', context=context)


@login_required
def create_post(request):
    if request.method == 'POST':
        news_type = request.POST.get('type')
        text = request.POST.get('description')
        title = request.POST.get('title')
        is_hacker_news = False

        by = request.user.first_name + " " + request.user.last_name
        
        # Create a new News object
        news = News(
            news_type=news_type,
            by=by,
            user=request.user,
            text=text,
            title=title,
            is_hacker_news=is_hacker_news
        )
        news.save()
        message = "news created successfully"
        return render(request, "news/create.html", {'message': message})
    return render(request, "news/create.html")



def get_profile(request):
    user_id = request.user.id
    user = User.objects.filter(id=user_id).first()


    user_data = {
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
        "username": user.username,
        "number_of_posts": 0
    }

    return render(request, 'news/profile.html', context=user_data)



def news_search(request):
    query = request.GET.get('q')
    news = News.objects.filter(title__icontains=query)
    context = {'news': news, 'query': query}
    return render(request, 'news/index.html', context)