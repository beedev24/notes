from django.db import models
from .misc import *
from django.db.models.signals import post_save
from django.db.models.deletion import CASCADE

class UserManager(models.Manager):
    def validate(self, form):
        errors = {}
        usernameCheck = self.filter(username=form['username'])
        if usernameCheck:
            errors['username'] = "Username unavailable"
        if form['password'] != form['confirm']:
            errors['password'] = 'Passwords do not match'
        return errors

class User(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    permissions = models.IntegerField(default=0)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    objects = UserManager()
    def __str__(self):
        return f'{self.firstName} {self.lastName}'

class Profile(models.Model):
    img = models.ImageField(upload_to='profileImgs', default='hive.jpg')
    user = models.OneToOneField(User, unique=True, on_delete=CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.user.firstName} {self.user.lastName} Profile'

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        User.objects.create(user=instance)
        post_save.connect(create_user_profile, sender=User)

class School(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class Institution(models.Model):
    img = models.ImageField(upload_to='schoolImgs', default='beeDevClassRoom.png')
    school = models.OneToOneField(School, unique=True, on_delete=CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.school.name} Institution'

def create_school_institution(sender, instance, created, **kwargs):
    if created:
        School.objects.create(school=instance)
        post_save.connect(create_school_institution, sender=School)
    
class Subject(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    length = models.CharField(max_length=255, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.subject

class Topic(models.Model):
    img = models.ImageField(upload_to='schoolImgs', default='beeDevClassRoom.png')
    subject = models.OneToOneField(Subject, unique=True, on_delete=CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.subject.title} Topic'

def create_subject_topic(sender, instance, created, **kwargs):
    if created:
        Subject.objects.create(subject=instance)
        post_save.connect(create_subject_topic, sender=Subject)

class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    noteUrl = models.CharField(max_length=255, blank=True)
    resourceUrl = models.CharField(max_length=255, blank=True)
    code = models.TextField(blank=True)
    codeUrl = models.CharField(max_length=255, blank=True)
    access = models.BooleanField(default=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name='noteUser', on_delete=CASCADE)
    school = models.ForeignKey(School, related_name='noteSchool', on_delete=CASCADE, blank=True)
    subject = models.ForeignKey(Subject, related_name='noteSubject', on_delete=CASCADE, blank=True)
    def __str__(self):
        return self.title

class Memo(models.Model):
    img = models.ImageField(upload_to='noteImgs', default='notebook.png')
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    note = models.OneToOneField(Note, unique=True, on_delete=CASCADE)
    def __str__(self):
        return f'{self.note.title} Memo'

def create_note_memo(sender, instance, created, **kwargs):
    if created:
        Note.objects.create(note=instance)
        post_save.connect(create_note_memo, sender=Note)



