# notes_app/urls.py
from django.contrib import admin
from django.urls import path
from .views import RegisterView, LoginView
from notes.views import NoteListCreateView, NoteDetailView

urlpatterns = [
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/notes/', NoteListCreateView.as_view(), name='note-list'),
    path('api/notes/<id>/', NoteDetailView.as_view(), name='note-detail'),
]