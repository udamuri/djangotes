from django.contrib import admin

from .models import Post, Category

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'slug')
    #list_filter = ['pub_date']
    search_fields = ['title']

admin.site.register(Post, PostAdmin)

class CategoryAdmin(admin.ModelAdmin):
    #list_display = ('name', 'slug', 'parent', 'pub_date', 'was_published_recently')
    #list_filter = ['pub_date']
    search_fields = ['name']

admin.site.register(Category, CategoryAdmin)
