from django.urls import path
from .views import (
    NotesListView,
    NotesDetailView,
    NotesCreateView,
    NotesUpdateView,
    NotesDeleteView
)


urlpatterns = [
    path('', NotesListView.as_view(), name='notes'),
    path('<int:pk>/', NotesDetailView.as_view(), name='notes-detail'),
    path('new/', NotesCreateView.as_view(), name='notes-create'),
    path('/<int:pk>/update/', NotesUpdateView.as_view(), name='notes-update'),
    path('/<int:pk>/delete/', NotesDeleteView.as_view(), name='notes-delete'),
]
