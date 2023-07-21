from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    path('registration/', views.registration_view, name='registration'),
    path('index', views.book_list, name='book_list'),
    path('add/', views.book_add, name='book_add'),
    path('edit/<int:book_id>/', views.book_edit, name='book_edit'),
    path('delete/<int:book_id>/', views.book_delete, name='book_delete'),
    path('details/<int:book_id>/', views.book_details, name='book_details'),
]
