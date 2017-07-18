from django.contrib import admin
from .models import Crypt

class AnswerInline(admin.StackedInline):
    #model = Answer
    extra = 0

class CryptRecDataAdmin(admin.ModelAdmin):
	list_display = ('name', 'rollno','mobileno','email')
	inlines = [AnswerInline]

admin.site.register(Crypt)
# Register your models here.
