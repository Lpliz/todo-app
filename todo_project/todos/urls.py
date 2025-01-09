"""
URL configuration for todo_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, path
from .views import ToDoListDisplay, ToDoCreate, ToDoDelete, ToDoEdit, ToDoGetDetail, DeleteAllTasks

urlpatterns = [
    path('admin/', admin.site.urls),
    path('display', ToDoListDisplay.as_view(), name='todo-list-display'),
    path('add', ToDoCreate.as_view(), name='todo-create'),
    path('display/<int:pk>', ToDoGetDetail.as_view(), name='todo-detailed'),
    path('edit/<int:pk>', ToDoEdit.as_view(), name='todo-edit'),
    path('delete/<int:pk>', ToDoDelete.as_view(), name='todo-delete'),
    path('deleteAll', DeleteAllTasks.as_view(), name='todo-delete-all'),
]
