from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader
from .models import Note, Label
from django.contrib.auth.forms import User
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required


def index(request):
    search = request.GET.get('search', '')
    if request.user.is_authenticated:
        template = loader.get_template('index.html')
        context = {'notes': Note.objects.filter(user=request.user, title__icontains=search), 'search_value':search}
        return HttpResponse(template.render(context, request))
    else:
        return redirect('login')


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')

    template = loader.get_template('login.html')
    context = {}
    return HttpResponse(template.render(context, request))


def signup(request):
    if request.method == "POST":
        # pasiimame reikšmes iš registracijos formos
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        User.objects.create_user(username, email, password)
        return redirect('index')
    elif request.method == "GET":
        template = loader.get_template('signup.html')
        context = {}
        return HttpResponse(template.render(context, request))


def create_note(request):
    if request.method == "POST":
        notename = request.POST['notename']
        notetext = request.POST['notetext']
        notelabel = request.POST['notelabel']
        if notelabel == 'null':
            notelabel = None
        # label = Label.objects.find(notelabel)
        Note.objects.create(title=notename, text=notetext, user=request.user, label_id=notelabel)
        return redirect('index')
    elif request.method == "GET":
        template = loader.get_template('create_note.html')
        context = {'labels': Label.objects.filter(user=request.user)}
        return HttpResponse(template.render(context, request))


def logout_user(request):
    logout(request)
    return redirect('index')


def label(request):
    template = loader.get_template('labels.html')
    context = {'labels': Label.objects.filter(user=request.user)}
    return HttpResponse(template.render(context, request))


def label_notes(request, label_id):
    template = loader.get_template('label_notes.html')
    context = {'notes': Note.objects.filter(label__id=label_id, user=request.user)}
    return HttpResponse(template.render(context, request))


def edit_note(request, note_id):
    if request.method == "POST":
        notename = request.POST['notename']
        notetext = request.POST['notetext']
        notelabel = request.POST['notelabel']
        if notelabel == 'null':
            notelabel = None
        note = Note.objects.get(id=note_id)
        note.title = notename
        note.text = notetext
        note.label_id = notelabel
        note.save()
        return redirect('index')
    elif request.method == "GET":
        template = loader.get_template('edit_note.html')
        context = {'labels': Label.objects.filter(user=request.user), 'note': Note.objects.get(id=note_id)}
        return HttpResponse(template.render(context, request))


def delete_note(request, note_id):
    note = Note.objects.get(id=note_id)
    note.delete()
    return redirect('index')


