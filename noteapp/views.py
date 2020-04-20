from django.shortcuts import render
from django.http import HttpResponse
from .models import Note
# Create your views here.

#show allnotes



def allnotes(request):
    allnotes = Note.objects.all()

    context = {
       'allnotes' : allnotes

    }
    return render (request, 'allnotes.html' , context)
    #return HttpResponse('<h1>Hello world<h1>')

#show one note
#def onenote(request ,id):
    #shownote = Note.objects.get(id=id)
    #ontext = {
    #    'shownote' : shownote
    #}
    #return render (request,'onenote.html' , context)
def onenote(request ,slug):
    shownote = Note.objects.get(slug=slug)
    context = {
        'shownote' : shownote
    }
    return render (request,'onenote.html' , context)
