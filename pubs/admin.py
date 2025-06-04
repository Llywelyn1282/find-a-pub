from django.contrib import admin
from .models import Pub, Comment, OpeningHour
from django_summernote.admin import SummernoteModelAdmin

class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status')
    search_fields = ['title']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


class OpeningHoursInline(admin.TabularInline):
    model = OpeningHour
    ordering = ['day']
    fields = ('day', 'opening_time', 'closing_time', 'closed')
    max_num = 7

@admin.register(Pub)
class PubAdmin(admin.ModelAdmin):
    inlines = [OpeningHoursInline]

admin.site.register(Comment)
