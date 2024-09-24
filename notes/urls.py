"""
URL configuration for notes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from notesapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("notes/add/",views.NotesCreateView.as_view(),name="notes-add"),
    # path("notes/edit/",views.NotesUpdateView.as_view(),name="notes-edit"),
    path("notes/all/",views.NotesListView.as_view(),name="notes-list"),
    # path("notes/<int:pk>/",views.NotesDetailView.as_view(),name="notes-detail"),
    path("notes/<int:pk>/remove/",views.NotesDeleteView.as_view(),name="notes-delete"),
    path("notes/remove/all/",views.NotesAllDeleteView.as_view(),name="notes-all-delete")
    

]
