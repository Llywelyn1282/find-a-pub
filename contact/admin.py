from django.contrib import admin
from .models import ContactForm
from django_summernote.admin import SummernoteModelAdmin


@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):

    list_display = ('message', 'read',)
