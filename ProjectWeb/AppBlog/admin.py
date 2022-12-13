from django.contrib import admin

from AppBlog.models import Post, Categoria

class CategoriaAdmin (admin.ModelAdmin):
    readonly_fields = ['created' , 'updated',]

class PostAdmin (admin.ModelAdmin):
    readonly_fields = ['created' , 'updated']

# Register your models here.
admin.site.register (Categoria, CategoriaAdmin)
admin.site.register (Post, PostAdmin)
