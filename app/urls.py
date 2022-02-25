from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),
    path('logReg/', views.logReg),
    path('register/', views.register),
    path('login/', views.login),
    path('logout/', views.logout),
    path('schools/', views.schools),
    path('schools/<int:school_id>/notes/', views.schoolNotes),
    path('schools/<int_school_id//notes/<int:note_id>/view/', views.viewSchoolNote),
    path('subjects/', views.subjects),
    path('subjects/<int:subject_id>/notes/', views.subjectNotes),
    path('subjects/<int:subject_id>/notes/<int:note_id>/views/', views.viewSubjectNotes),
    path('notes/', views.notes),
    path('notes/<int:note_id>/view/', views.viewNote),
    # Admin
    path('theAdmin/', views.theAdmin),
    path('theAdmin/school-subject/', views.schoolsSubjects),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)