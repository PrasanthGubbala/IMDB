import json
import random

from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect
import requests
from IMDB.settings import IMDB_FILE


def main(request):
    dict_data = json.loads(open(IMDB_FILE).read())
    list = dict_data['filmography']
    show_data = random.choice(list)
    return render(request, 'main.html',{'data':show_data})

def search_movie(request):
    movie = request.GET.get('movie')
    dict_data = json.loads(open(IMDB_FILE).read())
    list = dict_data['filmography']
    for mv in list:
        if movie in mv['title']:
            return render(request,'movie_details.html',{'data':mv})
        else:
            messages.error(request,'No Such Movie In Our Data-Base')
            return redirect('main')