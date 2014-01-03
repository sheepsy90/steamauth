from django.core.context_processors import csrf
from django.http import HttpResponse
from django.shortcuts import render, render_to_response

# Create your views here.


def index(request):
    c = {}
    c.update(csrf(request))
    return render_to_response("index.html", c)