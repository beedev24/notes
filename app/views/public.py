from django.shortcuts import render, redirect
from django.contrib import messages
from ..models import *

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

def viewSchoolNote(request, school_id, note_id):
    if 'user_id' not in request.session:
        note = Note.objects.get(id=note_id)
        school = School.objects.get(id=school_id)
        subjects = Subject.objects.all().values()
        users = User.objects.all().values()
        notes = Note.objects.all().values().order_by('title')
        context = {
            'note': note,
            'school': school,
            'subjects': subjects,
            'users': users,
        }
        return render(request, 'viewNote.html', context)
    else:
        user = User.objects.get(id=request.session['user_id'])
        note = Note.objects.get(id=note_id)
        school = School.objects.get(id=school_id)
        subjects = Subject.objects.all().values()
        users = User.objects.all().values()
        notes = Note.objects.all().values().order_by('title')
        context = {
            'user': user,
            'note': note,
            'school': school,
            'subjects': subjects,
            'users': users,
            'notes': notes,
        }
        return render(request, 'logged/viewNote.html', context)

def subjectNotes(request, subject_id):
    if 'user_id' not in request.session:
        subject = Subject.objects.get(id=subject_id)
        notes = Note.objects.all().values().order_by('title')
        schools = School.objects.all().values()
        context = {
            'subject': subject,
            'notes': notes,
            'schools': schools
        }
        return render(request, 'subjectNotes.html', context)
    else:
        user = User.objects.get(id=request.session['user_id'])
        subject = Subject.objects.get(id=subject_id)
        notes = Note.objects.all().values().order_by('title')
        schools = School.objects.all().values()
        context = {
            'user': user,
            'subject': subject,
            'notes': notes,
            'schools': schools
        }
        return render(request, 'logged/subjectNotes.html', context)

def viewSubjectNote(request, subject_id, note_id):
    if 'user_id' not in request.session:
        note = Note.objects.get(id=note_id)
        schools = School.objects.all().values()
        subject = Subject.objects.get(id=subject_id)
        users = User.objects.all().values()
        notes = Note.objects.all().values().order_by('title')
        context = {
            'note': note,
            'schools': schools,
            'subject': subject,
            'users': users,
            'notes': notes,
        }
        return render(request, 'viewNote.html', context)
    else:
        user = User.objects.get(id=request.session['user_id'])
        note = Note.objects.get(id=note_id)
        schools = School.objects.all().values()
        subject = Subject.objects.get(id=subject_id)
        users = User.objects.all().values()
        notes = Note.objects.all().values().order_by('title')
        context = {
            'user': user,
            'note': note,
            'schools': schools,
            'subject': subject,
            'users': users,
            'notes': notes,
        }
        return render(request, 'logged/viewNote.html', context)

def viewNote(request, note_id):
    if 'user_id' not in request.session:
        note = Note.objects.get(id=note_id)
        schools = School.objects.all().values()
        subjects = Subject.objects.all().values()
        users = User.objects.all().values()
        context = {
            'note': note,
            'schools': schools,
            'subjects': subjects,
            'users': users,
        }
        return render(request, 'viewNote.html', context)
    else:
        user = User.objects.get(id=request.session['user_id'])
        note = Note.objects.get(id=note_id)
        schools = School.objects.all().values()
        subjects = Subject.objects.all().values()
        users = User.objects.all().values()
        context = {
            'user': user,
            'note': note,
            'schools': schools,
            'subjects': subjects,
            'users': users,
        }
        return render(request, 'logged/viewNote.html', context)
        
        

# 9 public functions