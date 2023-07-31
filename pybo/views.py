from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Diary, Todolist
from .forms import DiaryForm, TodoForm
from django.utils import timezone
# Create your views here.

def index(request):
    return render(request, 'pybo/site_home.html')

def diary(request):
    diary_list = Diary.objects.order_by('-create_date')
    context = {'diary_list' : diary_list}
    return render(request, 'pybo/diary_list.html', context)

def diary_detail(request, diary_id):
    diary = Diary.objects.get(id=diary_id)
    context = {'diary': diary}
    return render(request, 'pybo/diary_detail.html', context)

def diary_create(request):
    if request.method == 'POST':
        form = DiaryForm(request.POST)
        if form.is_valid():
            diary = form.save(commit=False)  #임시저장
            diary.create_date = timezone.now()
            diary.save()  #실제저장
            return redirect('pybo:diary')
    else:
         form = DiaryForm()
    context = {'form' : form}
    return render(request, 'pybo/diary_create.html', context)

def todolist(request):
    todolist =  Todolist.objects.order_by('end_date')
    context = {'todolist': todolist}
    return render(request, 'pybo/todolist.html', context)

def todolsit_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect('pybo:todolist')
    else:
        form = TodoForm()
    context = {'form': form}
    return render(request, 'pybo/todo_create.html', context)