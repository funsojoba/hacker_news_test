from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from django.db.models import Q

from django.contrib.auth.models import User
from .models import News
from haystack.generic_views import SearchView

from .forms import NewsForm

# Create your views here.


def home(request):
    message = request.GET.get('message')
    filter_type = request.GET.get('type')
    
    data = News.objects.all()

    if filter_type:
        data = data.filter(news_type__icontains=filter_type)
    context ={
        'year':timezone.now().year,
        'data': data,
        'user': request.user,
        'message': message,
        'filter_type':filter_type
    }
    return render(request, 'news/index.html', context)



def details(request, id):
    news = get_object_or_404(News, id=id)
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
                'time': news.time,
                'can_edit': news.user == request.user,
                'url': news.url,
                'year': timezone.now().year
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


@login_required
def news_update(request, id):
    news = get_object_or_404(News, id=id)

    if request.method == 'POST':
        form = NewsForm(request.POST, instance=news)
        if form.is_valid():
            form.save()
            return redirect('details', id=news.id)
    else:
        form = NewsForm(instance=news)

    context = {'form': form, 'news': news}
    return render(request, 'news/news_update.html', context)




def news_search(request):
    query = request.GET.get('q')
    news = News.objects.filter(
        Q(text__icontains=query) | Q(title__icontains=query) | Q(by__icontains=query))
    context = {'news': news, 'query': query}
    return render(request, 'news/index.html', context)



def page_not_found(request, exception):
    return render(request, '404.html', status=404)