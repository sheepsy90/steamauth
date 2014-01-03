from django.core.context_processors import csrf
from django.http import HttpResponse
from django.shortcuts import render, render_to_response

# Create your views here.


def index(request):
    c = {}
    c.update(csrf(request))
    return render_to_response("index.html", c)


def steam_success(request):
    x = []
    for key in request.GET:
        if "openid" in key:
            x.append([key, request.GET[key]])
    return render_to_response('steam_success.html', {"a" :  x})