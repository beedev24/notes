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
    path('subjects/<int:subject_id>/notes/<int:note_id>/views/', views.viewSubjectNote),
    path('notes/', views.notes),
    path('notes/<int:note_id>/view/', views.viewNote),
    # Admin
    path('theAdmin/', views.theAdmin),
    path('theAdmin/<int:user_id>/profile/', views.profile),
    path('theAdmin/<int:user_id>/profile/user/update/', views.updateUser),
    path('theAdmin/<int:user_id>/profile/user/permissions/update/', views.updateUserPermission),
    path('theAdmin/<int:user_id>/profile/profile/update/', views.updateProfile),
    # schools / subjects
    path('theAdmin/school-subject/', views.schoolsSubjects),
    path('theAdmin/school-subject/school/create/', views.createSchool),
    path('theAdmin/school-subject/school/<int:school_id>/update/', views.updateSchool),
    path('theAdmin/school-subject/school/<int:school_id>/institution/update/', views.updateInstitution),
    path('theAdmin/school-subject/school/<int:school_id>/delete/', views.deleteSchool),
    path('theAdmin/school-subject/subject/create/', views.createSubject),
    path('theAdmin/school-subject/subject/<int:subject_id>/update/', views.updateSubject),
    path('theAdmin/school-subject/subject/<int:subject_id>/topic/update/', views.updateTopic),
    path('theAdmin/school-subject/subject/<int:subject_id>/delete/', views.deleteSubject),
    # Notes
    path('theAdmin/notes/', views.theNotes),
    path('theAdmin/notes/create/', views.createNote),
    path('theAdmin/notes/<int:note_id>/edit/', views.editNote),
    path('theAdmin/notes/<int:note_id>/update/', views.updateNote),
    path('theAdmin/notes/<int:note_id>/note-access/update/', views.updateNoteAccess),
    path('theAdmin/notes/<int:note_id>/note-url/update/', views.updateNoteUrl),
    path('theAdmin/notes/<int:note_id>/note_resource/update/', views.updateResourceUrl),
    path('theAdmin/notes/<int:note_id>/note-code/update/', views.updateNoteCode),
    path('theAdmin/notes/<int:note_id>/note-codeUrl/update/', views.updateNoteCodeUrl),
    path('theAdmin/notes/<int:note_id>/memo/update/', views.updateMemo),
    path('theAdmin/notes/<int:note_id>/delete/', views.deleteNote),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)