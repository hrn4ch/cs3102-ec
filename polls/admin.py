from django.contrib import admin
from .models import Topic

class TopicAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title']}),
        (None, {'fields': ['desc']}),
        (None, {'fields': ['image']}),
        (None, {'fields': ['postURL']}),
    ]
    list_display = ('title', 'desc', 'image', 'postURL')
    search_fields = ['title']

admin.site.register(Topic, TopicAdmin)
