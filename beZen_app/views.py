from django.shortcuts import render,redirect
from .models import Note
from datetime import datetime
# Create your views here.

def index(request):
    notes = Note.objects.all()
    important = Note.objects.filter(important=True)
    return render(request,'index.html',{'notes':notes,'important':important})

def addNewNote(request):
    heading = request.POST['heading']
    tagline = request.POST['tagline']
    content = request.POST['content']
    Note.objects.create(heading=heading,tagline=tagline,content=content,created=datetime.now(),lastUpdated=datetime.now())
    return redirect(index)

def updateNote(request):
    id = request.POST['id']
    heading = request.POST['heading']
    tagline = request.POST['tagline']
    content = request.POST['content']
    Note.objects.filter(id=id).update(heading=heading,tagline=tagline,content=content,lastUpdated=datetime.now())
    return redirect(index)

def pin(request):
    id = request.GET['id']
    Note.objects.filter(id=id).update(important=True)
    return redirect(index)

def unpin(request):
    id = request.GET['id']
    Note.objects.filter(id=id).update(important=False)
    return redirect(index)

def delete(request):
    id = request.GET['id']
    Note.objects.filter(id=id).delete()
    return redirect(index)