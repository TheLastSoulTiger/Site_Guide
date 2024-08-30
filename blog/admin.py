from django.contrib import admin
from .models import Post, Tour
from .models import Tour, TourImage


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date')
    search_fields = ('title', 'content')

class TourImageInline(admin.TabularInline):
    model = TourImage
    extra = 1

class TourAdmin(admin.ModelAdmin):
    inlines = [TourImageInline]

admin.site.register(Tour, TourAdmin)
admin.site.register(Post, PostAdmin)