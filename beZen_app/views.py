from django.shortcuts import render,redirect
from .models import Note
from datetime import datetime
# Create your views here.

def index(request):
    notes = Note.objects.all()
    return render(request,'index.html',{'notes':notes})

def addNewNote(request):
    heading = request.POST['heading']
    tagline = request.POST['tagline']
    content = request.POST['content']
    Note.objects.create(heading=heading,tagline=tagline,content=content,created=datetime.now(),lastUpdated=datetime.now())
    return redirect(index)
