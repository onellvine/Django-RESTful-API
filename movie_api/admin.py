from django.contrib import admin
from .models import SysUser, Movie, Comment


@admin.register(SysUser)
class SysUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'phone', 'is_staff', 'is_active')
    search_fields = ('username', 'phone')
    search_filter = ('is_staff', 'is_active')

    fieldsets = (
        (None, {
            'fields': ('username','phone','password')
        }),
        ('Config', {
            'fields': ('is_staff', 'is_active')
        })
    )

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'released', 'comments')
    search_fields = ('title', 'genre')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user_id','movie_id', 'comment')
    search_fields = ('comment',)

