from django.contrib import admin
from museum_object_manager.models import MuseumRecord
from django.utils.safestring import mark_safe

class MuseumRecordAdmin(admin.ModelAdmin):
    exclude = ('raw_data',)
    readonly_fields = ('img_preview',)

    def img_preview(self, instance):
        return '<img src="%s">' % instance.get_primary_image
    img_preview.short_description = "Api Img"
    img_preview.allow_tags = True

admin.site.register(MuseumRecord,MuseumRecordAdmin)
