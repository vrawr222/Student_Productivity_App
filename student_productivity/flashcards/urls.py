from django.urls import path
from . import views

urlpatterns = [
    path('', views.flashcard_list, name='flashcard_list'),
    path('create/', views.create_flashcard, name='create_flashcard'),
    path('delete/<int:id>/', views.delete_flashcard, name='delete_flashcard'),
    path('update/<int:id>/<str:difficulty>/', views.update_flashcard, name='update_flashcard'),
path('review/', views.review_flashcards, name='review_flashcards_start'),
path('review/<int:index>/', views.review_flashcards, name='review_flashcards'),]