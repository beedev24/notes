from django.shortcuts import render, redirect
from django.contrib import messages
from ..models import *

# Landing pages 5
def theAdmin(request):
    if 'user_id' not in request.session:
        messages.error(request, "Page is protected")
        return redirect('/')
    else:
        user = User.objects.get(id=request.session['user_id'])
        users = User.objects.all().values().order_by('createdAt')
        context = {
            'user': user,
            'users': users,
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
        theUser = User.objects.get(id=request.session['user_id'])
        context = {
            'user': user,
            'theUser': theUser,
        }
        return render(request, 'logged/admin/profile.html', context)

def editSchool(request, school_id):
    if 'user_id' not in request.session:
        messages.error(request, "Page is protected")
        return redirect('/')
    else:
        user = User.objects.get(id=request.session['user_id'])
        school = School.objects.get(id=school_id)
        context ={
            'user': user,
            'school': school,
        }
        return render(request, 'logged/admin/editSchool.html', context)

def editSubject(request, subject_id):
    if 'user_id' not in request.session:
        messages.error(request, "Page is protected")
        return redirect('/')
    else:
        user = User.objects.get(id=request.session['user_id'])
        subject = Subject.objects.get(id=subject_id)
        context ={
            'user': user,
            'subject': subject,
        }
        return render(request, 'logged/admin/editSubject.html', context)

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


# Create Routes 3
def createSchool(request):
    School.objects.create(
        name = request.POST['name'],
        description = request.POST['description'],
    )
    messages.error(request, 'School Created')
    return redirect('/theAdmin/school-subject/')

def createSubject(request):
    Subject.objects.create(
        title = request.POST['title'],
        description = request.POST['description'],
        length = request.POST['length'],
    )
    messages.error(request, 'Subject created')
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
    messages.error(request, 'Note created')
    return redirect('/theAdmin/notes/')


# Update Routes 14
def updateUser(request, user_id):
    toUpdate = User.objects.get(id=user_id)
    toUpdate.firstName = request.POST['firstName']
    toUpdate.lastName = request.POST['lastName']
    toUpdate.save()
    messages.error(request, 'User updated')
    return redirect('/theAdmin/')

def updateUserAdmin(request, user_id):
    toUpdate = User.objects.get(id=user_id)
    toUpdate.permissions = 24
    toUpdate.save()
    messages.error(request, 'User permissions changed to Admin')
    return redirect('/theAdmin/')

def updateUserContributor(request, user_id):
    toUpdate = User.objects.get(id=user_id)
    toUpdate.permissions = 0
    toUpdate.save()
    messages.error(request, 'User permissions changed to Contributor')
    return redirect('/theAdmin/')

def updateProfile(request, user_id):
    toUpdate = User.objects.get(id=user_id)
    toUpdate.profile.img = request.FILES['img']
    toUpdate.save()
    messages.error(request, 'User Profile Images updated')
    return redirect('/theAdmin/')

def updateSchool(request, school_id):
    toUpdate = School.objects.get(id=school_id)
    toUpdate.name = request.POST['name']
    toUpdate.description = request.POST['description']
    toUpdate.save()
    messages.error(request, 'School information updated')
    return redirect(f'/theAdmin/school-subject/school/{school_id}/edit/')

def updateInstitution(request, school_id):
    toUpdate = School.objects.get(id=school_id)
    toUpdate.institution.img = request.FILES['img']
    toUpdate.save()
    messages.error(request, 'School Image updated')
    return redirect(f'/theAdmin/school-subject/school/{school_id}/edit/')

def updateSubject(request, subject_id):
    toUpdate = Subject.objects.get(id=subject_id)
    toUpdate.title = request.POST['title']
    toUpdate.description = request.POST['description']
    toUpdate.length = request.POST['length']
    toUpdate.save()
    messages.error(request, 'Subject information updated')
    return redirect(f'/theAdmin/school-subject/subject/{subject_id}/edit/')

def updateTopic(request, subject_id):
    toUpdate = Subject.objects.get(id=subject_id)
    toUpdate.topic.img = request.FILES['img']
    toUpdate.save()
    messages.error(request, 'Subject image updated')
    return redirect(f'/theAdmin/school-subject/subject/{subject_id}/edit/')

def updateNote(request, note_id):
    toUpdate = Note.objects.get(id=note_id)
    toUpdate.title = request.POST['title']
    toUpdate.content = request.POST['content']
    toUpdate.save()
    messages.error(request, 'Note information updated')
    return redirect('/theAdmin/notes/')

def updateNoteSchool(request, note_id):
    toUpdate = Note.objects.get(id=note_id)
    toUpdate.school_id = request.POST['school']
    toUpdate.save()
    messages.error(request, 'Note School updated')
    return redirect('/theAdmin/notes/')

def updateNoteSubject(request, note_id):
    toUpdate = Note.objects.get(id=note_id)
    toUpdate.subject_id = request.POST['subject']
    toUpdate.save()
    messages.error(requst, 'Note Subject updated')
    return redirect('/theAdmin/notes/')

def updateNoteAccess(request, note_id):
    toUpdate = Note.objects.get(id=note_id)
    toUpdate.access = request.POST['access']
    toUpdate.save()
    messages.error(request, 'Note Privacy updated')
    return redirect('/theAdmin/notes/')

def updateNoteUrl(request, note_id):
    toUpdate = Note.objects.get(id=note_id)
    toUpdate.noteUrl = request.POST['noteUrl']
    toUpdate.save()
    messages.error(request, 'Note Link updated')
    return redirect('/theAdmin/notes/')

def updateResourceUrl(request, note_id):
    toUpdate = Note.objects.get(id=note_id)
    toUpdate.resourceUrl = request.POST['resourceUrl']
    toUpdate.save()
    messages.error(request, 'Note Resource Link updated')
    return redirect('/theAdmin/notes/')

def updateNoteCode(request, note_id):
    toUpdate = Note.objects.get(id=note_id)
    toUpdate.code = request.POST['code']
    toUpdate.save()
    messages.error(request, 'Note Code block updated')
    return redirect('/theAdmin/notes/')

def updateNoteCodeUrl(request, note_id):
    toUpdate = Note.objects.get(id=note_id)
    toUpdate.codeUrl = request.POST['codeUrl']
    toUpdate.save()
    messages.error(request, 'Note Code Link updated')
    return redirect('/theAdmin/notes/')

def updateMemo(request, note_id):
    toUpdate = Note.objects.get(id=note_id)
    toUpdate.memo.img = request.FILES['img']
    toUpdate.save()
    messages.error(request, 'Note Image updated')
    return redirect('/theAdmin/notes/')


# Delete Routes 3
def deleteSchool(request, school_id):
    toDelete = School.objects.get(id=school_id)
    toDelete.delete()
    messages.error(request, 'School Deleted')
    return redirect('/theAdmin/school-subject/')

def deleteSubject(request, subject_id):
    toDelete = Subject.objects.get(id=subject_id)
    toDelete.delete()
    messages.error(request, 'Subject Deleted')
    return redirect('/theAdmin/school-subject/')

def deleteNote(request, note_id):
    toDelete = Note.objects.get(id=note_id)
    toDelete.delete()
    messages.error(request, 'Note Deleted')
    return redirect('/theAdmin/notes/')