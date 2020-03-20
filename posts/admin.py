from django.contrib import admin
from .models import Post
from .models import Author
from .models import Comment

# Register your models here.


class PostInstanceInline(admin.StackedInline):
    model = Comment
    extra = 0


class PostModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'timestamp', 'updated', 'post_likes', 'genre', 'post_author']
    list_display_links = ['title', 'content', 'timestamp', 'updated', 'genre', 'post_likes']
    list_filter = ['timestamp']
    inlines = [PostInstanceInline]
    fields = ('title', 'content', 'timestamp', 'updated', 'genre', 'post_author')
    ordering = ['-timestamp']

    class Meta:
        model = Post


class AuthorModelAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'second_name', 'email']
    list_display_links = ['first_name', 'second_name', 'email']
    ordering = ['second_name', 'first_name']

    class Meta:
        model = Author


class CommentModelAdmin(admin.ModelAdmin):
    list_display = ['comment_text', 'comment_article']
    list_display_links = ['comment_text', 'comment_article']

    class Meta:
        model = Comment


admin.site.register(Post, PostModelAdmin)
admin.site.register(Author, AuthorModelAdmin)
admin.site.register(Comment, CommentModelAdmin)
