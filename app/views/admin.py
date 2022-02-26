from django.shortcuts import render, redirect
from django.contrib import messages
from ..models import *

# Landing pages
def theAdmin(request):
    if 'user_id' not in request.session:
        messages.error(request, "Page is protected")
        return redirect('/')
    else:
        user = User.objects.get(id=request.session['user_id'])
        context = {
            'user': user,
        }
        return render(request, 'logged/admin/theAdmin.html', context)

def schoolsSubjects(request):
    if 'user_id' not in request.session:
        messages.error(request, "Page is protected")
        return redirect('/')
    else:
        user = User.objects.get(id=request.session['user_id'])
        schools = School.objects.all().values()
        subjects = Subject.objects.all().values()
        context = {
            'user': user,
            'schools': schools,
            'subjects': subjects,
        }
        return render(request, 'logged/admin/schoolSubjects.html', context)

def theNotes(request):
    if 'user_id' not in request.session:
        messages.error(request, "Page is protected")
        return redirect('/')
    else:
        user = User.objects.get(id=request.session['user_id'])
        users = User.objects.all().values()
        notes = Note.objects.all().values()
        schools = School.objects.all().values()
        subjects = Subject.objects.all().values()
        context = {
            'user': user,
            'users': users,
            'notes': notes,
            'schools': schools,
            'subjects': subjects,
        }
        return render(request, 'logged/admin/notes.html', context)

def profile(request, user_id):
    if 'user_id' not in request.session:
        messages.error(request, "Page is protected")
        return redirect('/')
    else:
        user = User.objects.get(id=user_id)
        context = {
            'user': user,
        }
        return render(request, 'logged/admin/profile.html', context)

def editNote(request, note_id):
    if 'user_id' not in request.session:
        messages.error(request, "Page is protected")
        return redirect('/')
    else:
        user = User.objects.get(id=request.session['user_id'])
        note = Note.objects.get(id=note_id)
        users = User.objects.all().values()
        schools = School.objects.all().values()
        subjects = Subject.objects.all().values()
        context = {
            'user': user,
            'users': users,
            'note': note,
            'schools': schools,
            'subjects': subjects,
        }
        return render(request, 'logged/admin/editNote.html', context)


# Create Routes
def createSchool(request):
    School.objects.create(
        name = request.POST['name'],
        description = request.POST['description'],
    )
    return redirect('/theAdmin/school-subject/')

def createSubject(request):
    Subject.objects.create(
        title = request.POST['title'],
        description = request.POST['description'],
        length = request.POST['length'],
    )
    return redirect('/theAdmin/school-subject/')

def createNote(request):
    Note.objects.create(
        title = request.POST['title'],
        content = request.POST['content'],
        access = request.POST['access'],
        user_id = request.POST['user'],
        school_id = request.POST['school'],
        subject_id = request.POST['subject'],
    )
    return redirect('/theAdmin/notes/')


# Update Routes
def updateUser(request, user_id):
    toUpdate = User.objects.get(id=request.session['user_id'])
    toUpdate.firstName = request.POST['firstName']
    toUpdate.lastName = request.POST['lastName']
    toUpdate.save()
    return redirect('/theAdmin/')

def updateUserPermission(request, user_id):
    toUpdate = User.objects.get(id=request.session['user_id'])
    toUpdate.permissions = 24
    toUpdate.save()
    return redirect('/theAdmin/')

def updateProfile(request, user_id):
    toUpdate = User.objects.get(id=request.session['user_id'])
    toUpdate.profile.img = request.FILES['img']
    toUpdate.save()
    return redirect('/theAdmin/')

def updateSchool(request, school_id):
    toUpdate = School.objects.get(id=school_id)
    toUpdate.name = request.POST['name']
    toUpdate.description = request.POST['description']
    toUpdate.save()
    return redirect('/theAdmin/school-subject/')

def updateInstitution(request, school_id):
    toUpdate = School.objects.get(id=school_id)
    toUpdate.institution.img = request.FILES['img']
    toUpdate.save()
    return redirect('/theAdmin/school-subject/')

def updateSubject(request, subject_id):
    toUpdate = Subject.objects.get(id=subject_id)
    toUpdate.title = request.POST['title']
    toUpdate.description = request.POST['description']
    toUpdate.length = request.POST['length']
    toUpdate.save()
    return redirect('/theAdmin/school-subject/')

def updateTopic(request, subject_id):
    toUpdate = Subject.objects.get(id=subject_id)
    toUpdate.topic.img = request.FILES['img']
    toUpdate.save()
    return redirect('/theAdmin/school-subject/')

def updateNote(request, note_id):
    toUpdate = Note.objects.get(id=note_id)
    toUpdate.title = request.POST['title']
    toUpdate.content = request.POST['content']
    toUpdate.save()
    return redirect('/theAdmin/notes/')

def updateNoteAccess(request, note_id):
    toUpdate = Note.objects.get(id=note_id)
    toUpdate.access = request.POST['access']
    toUpdate.save()
    return redirect('/theAdmin/notes/')

def updateNoteUrl(request, note_id):
    toUpdate = Note.objects.get(id=note_id)
    toUpdate.noteUrl = request.POST['noteUrl']
    toUpdate.save()
    return redirect('/theAdmin/notes/')

def updateResourceUrl(request, note_id):
    toUpdate = Note.objects.get(id=note_id)
    toUpdate.resourceUrl = request.POST['resourceUrl']
    toUpdate.save()
    return redirect('/theAdmin/notes/')

def updateNoteCode(request, note_id):
    toUpdate = Note.objects.get(id=note_id)
    toUpdate.code = request.POST['code']
    return redirect('/theAdmin/notes/')

def updateNoteCodeUrl(request, note_id):
    toUpdate = Note.objects.get(id=note_id)
    toUpdate.codeUrl = request.POST['codeUrl']
    toUpdate.save()
    return redirect('/theAdmin/notes/')

def updateMemo(request, note_id):
    toUpdate = Note.objects.get(id=note_id)
    toUpdate.memo.img = request.FILES['img']
    toUpdate.save()
    return redirect('/theAdmin/notes/')

def deleteSchool(request, school_id):
    toDelete = School.objects.get(id=school_id)
    toDelete.delete()
    return redirect('/theAdmin/school-subject/')

def deleteSubject(request, subject_id):
    toDelete = Subject.objects.get(id=subject_id)
    toDelete.delete()
    return redirect('/theAdmin/school-subject/')

def deleteNote(request, note_id):
    toDelete = Note.objects.get(id=note_id)
    toDelete.delete()
    return redirect('/theAdmin/notes/')