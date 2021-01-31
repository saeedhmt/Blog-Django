from django.contrib import admin
from .models import *
# Register your models here.

# admin.site.register(CustomUser)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)
# admin.site.register(Dislike)
admin.site.register(Category)
admin.site.register(Tag)

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    pass