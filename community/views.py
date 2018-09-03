from django.shortcuts import render

from community.forms import *
from community.controller import getSearchList
from django.db import models
# Create your views here.
from django.http import HttpResponse

def search(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=Form()
        # print('here2')
        # return HttpResponse("GET method")
        # 최초 화면 생성시에는 GET 으로 들어간다.

    return render(request,'search.html',{'form':form})


def list(request):
    scrapperlist = Scrapper.objects.all()
    return render(request, 'list.html',{'scrapperlist':scrapperlist})



def view(request, num="1"):
    scrapper = Scrapper.objects.get(id=num)
    datas = request.POST
    context = {
        'scrapper' :  scrapper
    }
    return render(request, 'view.html', context)

def get_search_list(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = Form(request.POST)


    return getSearchList.get_searchs(request)


    # if form.is_valid():
    #     return getSearchList.get_searchs(request,{'form':form})
    # else :
    #     return render(request,'search.html',{'form':form,})

def temp(request):
    form = Form(request.POST)
    print("start")
    print("request.POST['required_keywords']   = " ,request.POST['required_keywords'])
    print("request.POST['required_keywords']   = ", request.POST['required_keywords'])
    print("request.POST['required_keywords']   = ", request.POST['required_keywords'])
    print("request.POST['required_keywords']   = ", request.POST['required_keywords'])
    print("request.POST['required_keywords']   = ", request.POST['required_keywords'])
    return render(request, 'temp.html',{'form':form,})