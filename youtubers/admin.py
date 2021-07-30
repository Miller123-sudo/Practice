from youtubers.models import Youtubers
from django.contrib import admin
from django.utils.html import format_html

# Register your models here.


class YtAdmin(admin.ModelAdmin):
    def Myphoto(self, object):
        return format_html('<img src={} width="40" />'.format(object.photo.url))

    list_display = ['id', 'Myphoto', 'name', 'subs_count', 'is_featured']
    search_fields = ('name', 'camera_type')
    list_filter = ('city', 'camera_type')
    list_display_links = ('id', 'name')
    list_editable = ('is_featured',)


admin.site.register(Youtubers, YtAdmin)
