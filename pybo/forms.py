from django import forms
from pybo.models import Diary, Todolist

class DiaryForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = ['subject', 'content']
        labels = {
            'subject' : '제목',
            'content' : '내용',
        }

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todolist
        fields = '__all__'
        labels = {
            'todo' : '할일',
            'end_date' : '마감날짜',
            'done' : '완료여부',
        }