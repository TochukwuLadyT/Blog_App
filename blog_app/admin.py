from django.contrib import admin

# Register your models here.
from .models import *


class StockAdmin(admin.ModelAdmin):
    list_display = ["title", "content", "published_date", "author"]
    list_filter = ["title"]
    search_fields = ["title", "content"]


admin.site.register(Post, StockAdmin)
# admin.site.register(Category)
admin.site.site_header = "Blog App"
admin.site.site_title = "Blog App"
