from django.contrib import admin
from .models import Song
# Register your models here.

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ("title", "language", "created", "updated")
    list_filter = ("language", "created", "updated")
    search_fields = ("title", "language")
    date_hierarchy = "created"
    ordering = ("created",)
    fields = ("title", "lyrics", "language")
    readonly_fields = ("created", "updated")
    #exclude = ("created", "updated")
    #prepopulated_fields = {"slug": ("title",)}
    #inlines = [SongInline]
    #actions = [make_published, make_draft]
    #list_editable = ("language",)
    #list_display_links = ("title",)
    #list_per_page = 10
    #list_max_show_all = 100
    #list_select_related = True
    #save_as