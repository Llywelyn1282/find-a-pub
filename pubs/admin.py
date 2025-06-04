from django.contrib import admin
from .models import Pub, Comment, OpeningHour
from django_summernote.admin import SummernoteModelAdmin


class OpeningHoursInline(admin.TabularInline):
    model = OpeningHour
    ordering = ['day']
    fields = ('day', 'opening_time', 'closing_time', 'closed')
    max_num = 7

@admin.register(Pub)
class PubAdmin(SummernoteModelAdmin):

    list_display = ('name', 'slug', 'status')
    search_fields = ['name', 'description']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('name',)}
    summernote_fields = ('description',)
    inlines = [OpeningHoursInline]

admin.site.register(Comment)
