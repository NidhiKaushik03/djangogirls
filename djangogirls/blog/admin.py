from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ("author", "title", "text")

admin.site.register(Post, PostAdmin)

admin.site.site_header = "Kaushik"
admin.site.index_title = "Nidhi"
admin.site.site_title = "Nidhi"

