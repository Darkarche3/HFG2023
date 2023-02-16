from django.contrib import admin

from .models import Project, Location, Participant, Category
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "location", "category")
    list_filter = ("location", "date", "category")
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Project, ProjectAdmin)
admin.site.register(Location)
admin.site.register(Participant)
admin.site.register(Category)