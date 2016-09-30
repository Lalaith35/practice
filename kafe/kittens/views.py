from django.shortcuts import render
from .models import Cat, Breed
from django.http import Http404, HttpResponseRedirect
# Create your views here.

def home (request):

    cats = Cat.objects.all()
    
    context = {'cat': cats}
    return render (request,"index.html", context)

def delete_cat(request, count):
    
    try:    
        Cat.objects.get(id=count).delete()
    except Cat.DoesNotExist:
        raise Http404
        

    cats = Cat.objects.all()
    
    context = {'cat': cats}

    return HttpResponseRedirect('/#two')
