from django.shortcuts import render
from django.http import HttpResponse


#最初に飛ぶページ 
def index(request):
    return render(request, 'index.html')