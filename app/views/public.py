from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

def index(request):
    if 'user_id' not in request.session:
        notes = Note.objects.all().values().order_by('title')
        users = User.objects.all().values()
        schools = School.objects.all().values().order_by('name')
        subjects = Subject.objects.all().values().order_by('title')
        context = {
            'notes': notes,
            'users': users,
            'schools': schools,
            'subjects': subjects,
        }
        return render(request, 'index.html', context)
    else:
        user = User.objects.get(id=request.session['user_id'])
        notes = Note.objects.all().values().order_by('title')
        users = User.objects.all().values()
        schools = School.objects.all().values().order_by('name')
        subjects = Subject.objects.all().values().order_by('title')
        context = {
            'user': user,
            'notes': notes,
            'users': users,
            'schools': schools,
            'subjects': subjects,
        }
        return render(request, 'logged/index.html', context)

def schools(request):
    if 'user_id' not in request.session:
        schools = School.objects.all().values().order_by('name')
        context = {
            'schools': schools,
        }
        return render(request, 'schools.html', context)
    else:
        user = User.objects.get(id=request.session['user_id'])
        schools = School.objects.all().values().order_by('name')
        context = {
            'user': user,
            'schools': schools,
        }
        return render(request, 'logged/schools.html', context)

def subjects(request):
    if 'user_id' not in request.session:
        subjects = Subject.objects.all().values().order_by('title')
        context = {
            'subjects': subjects,
        }
        return render(request, 'subjects.html', context)
    else:
        user = User.objects.get(id=request.session['user_id'])
        subjects = Subject.objects.all().values().order_by('title')
        context = {
            'user': user,
            'subjects': subjects,
        }
        return render(request, 'logged/subjects.html', context)

def notes(request):
    if 'user_id' not in request.session:
        notes = Note.objects.all().values().order_by('title')
        schools = School.objects.all().values()
        subjects = Subject.objects.all().values()
        context = {
            'notes': notes,
            'schools': schools,
            'subjects': subjects,
        }
        return render(request, 'notes.html', context)
    else:
        user = User.objects.get(id=request.session['user_id'])
        notes = Note.objects.all().values().order_by('title')
        schools = School.objects.all().values()
        subjects = Subject.objects.all().values()
        context = {
            'user': user,
            'notes': notes,
            'schools': schools,
            'subjects': subjects,
        }
        return render(request, 'logged/notes.html', context)

def schoolNotes(request, school_id):
    if 'user_id' not in request.session:
        school = School.objects.get(id=school_id)
        notes = Note.objects.all().values().order_by('title')
        subjects = Subject.objects.all().values()
        context = {
            'school': school,
            'notes': notes,
            'subjects': subjects,
        }
        return render(request, 'schoolNotes.html', context)
    else:
        user = User.objects.get(id=request.session['user_id'])
        school = School.objects.get(id=school_id)
        notes = Note.objects.all().values().order_by('title')
        subjects = Subject.objects.all().values()
        context = {
            'user': user,
            'school': school,
            'notes': notes,
            'subjects': subjects,
        }
        return render(request, 'logged/schoolNotes.html', context)

def subjectNotes(request, subject_id):
    pass

def viewNote(request, note_id):
    pass