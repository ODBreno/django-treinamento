from django.utils.html import format_html
from django.contrib import admin

from eventex.core.models import Contact, Speaker

class ContactInline(admin.TabularInline):
    model = Contact
    extra = 1


# Register your models here.
class SpeakerModelAdmin(admin.ModelAdmin):
    inlines=[ContactInline]
    prepopulated_fields={'slug': ('name',)}
    list_display = ['name', 'website']
    
    def website_link(self,obj):
        return format_html('<a href="{0}">{0}</a>',obj.website)

    website_link.short_description = 'website'

    def photo_img(self, obj):
        return format_html('<img width="32px" src="{} \>', obj.photo)

    photo_img.short_description = 'foto'

admin.site.register(Speaker, SpeakerModelAdmin)