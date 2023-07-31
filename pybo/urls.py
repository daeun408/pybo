
from django.urls import path, include
from . import views

app_name = 'pybo'

urlpatterns = [
    path('', views.index, name='index'),
    path('diary/', views.diary, name='diary'),
    path('diary/detail/<int:diary_id>/', views.diary_detail, name='diary_detail'),
    path('diary/create/', views.diary_create, name="diary_create"),
    path('todolist/', views.todolist, name="todolist"),
    path('todolist/create/', views.todolsit_create, name="todolsit_create")
]
