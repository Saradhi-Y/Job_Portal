from django.contrib import admin
from .models import Job, JobVacancyImage

# Inline class for multiple images
class JobVacancyImageInline(admin.TabularInline):
    model = JobVacancyImage
    extra = 1   # how many empty rows to show by default
    fields = ("image", "caption")

class JobAdmin(admin.ModelAdmin):
    list_display = ("title", "organization", "location", "application_deadline", "posted_on")
    search_fields = ("title", "organization")
    list_filter = ("organization", "location", "posted_on", "application_deadline")
    inlines = [JobVacancyImageInline]

# Register models
admin.site.register(Job, JobAdmin)
admin.site.register(JobVacancyImage)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'organization', 'location', 'vacancies', 'application_deadline', 'posted_on')
    search_fields = ('title', 'organization', 'location')
    list_filter = ('organization', 'location', 'application_deadline')
    ordering = ('-posted_on',)