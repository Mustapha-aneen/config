from django.contrib import admin
from jobs.models import PostJob
from jobs.models import Applicant,Comment
@admin.register(PostJob)
class JobsAdmin(admin.ModelAdmin):
  list_display = ("title","author","publish","status")
  list_filter = ("title","author","slug","status")
  prepopulated_fields = {'slug':('title',)}
 
@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
  list_display = ("firstname","lastname","job","email","date")
  list_filter = ("firstname","lastname","job","email","date")
# Register your models here.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
  list_display = ("name","email","created","active")
  search_fields = ("name","email")
