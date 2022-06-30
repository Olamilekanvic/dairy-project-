from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import Entry
from .forms import EntryForm

from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def add(request: HttpRequest) -> HttpResponse:
    form = EntryForm(request.POST)
    
    if request.method == 'POST':   
        form = EntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request=request, template_name='entries/add.html', context = {'form' : form}) 



@login_required
def index(request: HttpRequest) -> HttpResponse:

    if request.method == 'GET':

        entries = Entry.objects.order_by('-date_posted').filter(author=request.user)
        return render(request=request, template_name='entries/index.html', context = {'entries' : entries}) 
        

