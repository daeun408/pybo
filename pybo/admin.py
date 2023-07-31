from django.contrib import admin
from .models import Diary
from .models import Todolist
# Register your models here.

class DiaryAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Diary, DiaryAdmin)
admin.site.register(Todolist)