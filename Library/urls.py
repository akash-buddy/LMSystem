

from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('books/create/', views.book_create, name='book_create'),
    path('books/update/<int:pk>/', views.book_update, name='book_update'),
    path('books/delete/<int:pk>/', views.book_delete, name='book_delete'),
    path('members/', views.member_list, name='member_list'),
    path('members/create/', views.member_create, name='member_create'),
    path('members/update/<int:pk>/', views.member_update, name='member_update'),
    path('members/delete/<int:pk>/', views.member_delete, name='member_delete'),
    path('issue/', views.issue_book, name='issue_book'),
    path('return/<int:pk>/', views.return_book, name='return_book'),
    path('import-books/', views.import_books, name='import_books'),
]
