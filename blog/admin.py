from django.contrib import admin
from .models import Tag, Category, Page, Post

# Register your models here.
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name', 'slug')
    list_per_page = 10
    ordering = ('-id',)
    prepopulated_fields = {
        'slug' : ('name',),
    }
#admin.site.register(Tag, TagAdmin)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name', 'slug')
    list_per_page = 10
    ordering = ('-id',)
    prepopulated_fields = {
        'slug' : ('name',),
    }
#admin.site.register(Category, TagAdmin)

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'is_published')
    list_display_links = ('id', 'title')
    list_editable = ('is_published',)
    search_fields = ('id', 'title', 'slug')
    list_per_page = 10
    ordering = ('-id',)
    prepopulated_fields = {
        'slug' : ('title',),
    }
#admin.site.register(Category, TagAdmin)

@ admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'created_by', )
    list_display_links = ('id', 'title', )
    search_fields = ('id', 'slug', 'title', 'excerpt', 'content',)
    list_per_page = 50
    list_filter = ('category', 'is_published',)
    list_editable = ('is_published',)
    ordering = ('-id',)
    readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by')
    prepopulated_fields = {
        "slug": ('title',),
    }
    autocomplete_fields = ('tags', 'category')
