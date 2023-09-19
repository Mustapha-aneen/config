from django.contrib import admin
from pages.models import Post, Users,Json

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
  list_display = ("title","slug","publish","image")
  prepopulated_fields = {"slug":("title",)}
  
@admin.register(Json)
class JsonAdmin(admin.ModelAdmin):
  list_display = ("title","body")
@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ("username","email","password","register_date")
    list_filter = ("username","email","password","register_date")
