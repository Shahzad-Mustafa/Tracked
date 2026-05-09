from django.contrib import admin
from .models import SkillCategory, Skill, Project, Experience, Education, ContactMessage

admin.site.site_header = 'Shahzad Ali Portfolio Admin'
admin.site.site_title = 'Portfolio Admin'
admin.site.index_title = 'Content Management'


@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon', 'order']
    list_editable = ['order']
    ordering = ['order']


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'proficiency', 'order']
    list_editable = ['proficiency', 'order']
    list_filter = ['category']
    search_fields = ['name']
    ordering = ['category', 'order']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'project_type', 'is_active', 'order']
    list_editable = ['project_type', 'is_active', 'order']
    list_filter = ['project_type', 'is_active']
    search_fields = ['title', 'tagline']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['created_at']


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['company', 'role', 'start_date', 'end_label_display', 'is_current', 'order']
    list_editable = ['order', 'is_current']
    ordering = ['order']

    def end_label_display(self, obj):
        return obj.end_label
    end_label_display.short_description = 'End Date'


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['institution', 'degree', 'start_year', 'end_year', 'order']
    list_editable = ['order']


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'is_read', 'replied', 'created_at']
    list_filter = ['is_read', 'replied', 'created_at']
    list_editable = ['is_read', 'replied']
    search_fields = ['name', 'email', 'subject']
    readonly_fields = ['name', 'email', 'subject', 'message', 'ip_address', 'created_at']
    ordering = ['-created_at']
    actions = ['mark_as_read']

    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
    mark_as_read.short_description = 'Mark selected messages as read'
