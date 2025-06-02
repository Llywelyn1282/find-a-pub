from django.contrib import admin
from .models import Pub, Comment, OpeningHour


class OpeningHoursInline(admin.TabularInline):
    model = OpeningHour
    extra = 1
    ordering = ['day']
    fields = ('day', 'opening_time', 'closing_time', 'closed')
    max_num = 7

@admin.register(Pub)
class PubAdmin(admin.ModelAdmin):
    inlines = [OpeningHoursInline]

admin.site.register(Comment)
