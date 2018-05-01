from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from django.contrib.auth.decorators import login_required

import datetime

from .models import News, Order, CollaboratingOrganization, EducationalProject, Event, Employer, IndustrialProject,\
                    Sponsor, Startup, UserProfile


def index(request):
    if request.method == 'GET':
        now = datetime.datetime.now()
        all_news = News.objects.all().order_by('publication_date').reverse()
        return HttpResponse(render(request, 'index.html', {'now_time': now,
                                                           'posts': all_news}))
    else:
        return HttpResponse('error')


@login_required
def profile(request):
    if request.method == 'GET':
        projects = CollaboratingOrganization.objects.all()
        orders = Order.objects.all()
        return HttpResponse(render(request, 'account.html', {'posts': projects, 'orders': orders}))
    else:
        return HttpResponse('error')

@login_required
def newproject(request):
    if request.method == 'GET':
        return HttpResponse(render(request, 'newproject.html', {}))
    else:
        return HttpResponse('error')


def for_students(request):
    if request.method == 'GET':
        return HttpResponse(render(request, 'for_students.html', 
                                   {'active' : 'students'}))
    else:
        return HttpResponse('error')

    
def summer_schools(request):
    if request.method == 'GET':
        summer_schools = IndustrialProject.objects.all()
        return HttpResponse(render(request, 'clubs.html', {'posts': summer_schools}))
    else:
        return HttpResponse('error')


def clubs(request):
    if request.method == 'GET':
        clubs = EducationalProject.objects.all()
        return HttpResponse(render(request, 'summer_school.html', {'posts': clubs}))
    else:
        return HttpResponse('error')


def about(request):
    if request.method == 'GET':
        return HttpResponse(render(request, 'about.html',
                                   {'active' : 'about'}))
    else:
        return HttpResponse('error')

    
def news(request):
    if request.method == 'GET':
        all_news = News.objects.all()
        return HttpResponse('news')
    else:
        return HttpResponse('error')


def projects(request):
    if request.method == 'GET':
        projects = CollaboratingOrganization.objects.all()
        return HttpResponse(render(request, 'projects.html', {'posts': projects}))
    else:
        return HttpResponse('error')


def read_news(request, news_id):
    if request.method == 'GET':
        element = News.objects.get(id=news_id)
        return HttpResponse(render(request, 'read_news.html',
                                   {'title': element.title,
                                    'lines': element.text.split('\n'),
                                    'publication_date': element.publication_date,
                                    'logo_url': element.logo.url}))
    else:
        return HttpResponse('error')
