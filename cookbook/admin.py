from django.contrib import admin
from .models import Recipe, Comment, Submission
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    """Allows admin to manage recipes via the admin panel"""
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ('title', 'description')
    summernote_fields = ('description', 'ingredients', 'method')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Allows admin to manage comments on recipes via the admin panel"""
    list_display = ('name', 'body', 'recipe', 'created_on', 'approved')
    list_filter = ('approved', 'created_on',)
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    prepopulated_fields = {'submission_slug': ('submission_title',)}
    list_display = ('user', 'method')
