from .models import Category
from .models import Author
from .models import Post

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from django.contrib import admin


class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category


class AuthorResource(resources.ModelResource):
    class Meta:
        model = Author


class PostResource(resources.ModelResource):
    class Meta:
        model = Post

class CategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ["name"]
    list_display = ("name", "status", "creation_date")
    resource_class = CategoryResource


class AuthorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ["firstname", "lastname", "email"]
    list_display = ("firstname", "lastname", "email", "status", "creation_date")
    resource_class = AuthorResource


class PostAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ["title", "author", "category"]
    list_display = ("title", "author", "category", "status", "creation_date")
    

admin.site.register(Category, admin_class=CategoryAdmin)
admin.site.register(Author, admin_class=AuthorAdmin)
admin.site.register(Post, admin_class=PostAdmin)
