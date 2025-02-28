from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('delete_account/', views.delete_account, name='delete_account'),
    path('edit_account/', views.edit_account, name='edit_account'),
]