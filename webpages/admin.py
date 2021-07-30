from webpages.models import Slider, Team
from django.contrib import admin
from django.utils.html import format_html

# Register your models here.


class TeamAdmin(admin.ModelAdmin):
    def Myphoto(self, object):
        return format_html('<img src={} width="40" />'.format(object.photo.url))

    list_display = ['id', 'Myphoto', 'first_name', 'role', 'created_date']
    list_display_links = ('first_name', 'id')
    list_filter = ('role',)


admin.site.register(Slider)
admin.site.register(Team, TeamAdmin)
