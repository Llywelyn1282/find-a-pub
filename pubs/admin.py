from django.contrib import admin
from .models import Pub, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Pub)
class PubAdmin(SummernoteModelAdmin):

    list_display = ('name', 'slug', 'status')
    search_fields = ['name', 'description']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('name',)}
    summernote_fields = ('description',)


admin.site.register(Comment)
