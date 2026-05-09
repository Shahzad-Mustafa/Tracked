from datetime import timedelta

from django.contrib import admin
from django.db.models import Count
from django.shortcuts import render
from django.urls import path
from django.utils import timezone
from django_summernote.admin import SummernoteModelAdmin

from .models import (ContactMessage, Education, Experience, HeroBadge,
                     PageVisit, Profile, Project, Skill, SkillCategory)

admin.site.site_header = 'Portfolio Admin'
admin.site.site_title = 'Portfolio Admin'
admin.site.index_title = 'Content Management'


@admin.register(Profile)
class ProfileAdmin(SummernoteModelAdmin):
    summernote_fields = ('bio_detail',)
    fieldsets = (
        ('Identity', {'fields': ('name', 'tagline', 'avatar', 'is_available', 'available_label')}),
        ('Bio', {'fields': ('bio_short', 'bio_detail')}),
        ('Contact', {'fields': ('email', 'phone', 'whatsapp', 'location')}),
        ('Social Links', {'fields': ('github_url', 'linkedin_url', 'website_url')}),
        ('Hero Stats', {
            'description': 'Values and labels shown in the hero section chips',
            'fields': (
                ('total_projects', 'projects_label'),
                ('years_experience', 'experience_label'),
                ('sites_scraped', 'scraped_label'),
            ),
        }),
        ('About Metrics', {
            'description': 'Four stat cards in the About section',
            'fields': (
                ('metric1_value', 'metric1_label', 'metric1_icon'),
                ('metric2_value', 'metric2_label', 'metric2_icon'),
                ('metric3_value', 'metric3_label', 'metric3_icon'),
                ('metric4_value', 'metric4_label', 'metric4_icon'),
            ),
        }),
        ('Preferences', {'fields': ('open_to_remote', 'resume_label')}),
    )


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


@admin.register(HeroBadge)
class HeroBadgeAdmin(admin.ModelAdmin):
    list_display  = ['label', 'icon', 'position', 'order', 'is_active']
    list_editable = ['position', 'order', 'is_active']
    ordering      = ['order']


@admin.register(PageVisit)
class PageVisitAdmin(admin.ModelAdmin):
    list_display   = ['ip_address', 'browser', 'os', 'device_type', 'path', 'visited_at']
    list_filter    = ['device_type', 'browser', 'visited_at']
    search_fields  = ['ip_address', 'browser', 'os', 'path']
    readonly_fields = [f.name for f in PageVisit._meta.get_fields()
                       if hasattr(f, 'name') and f.name != 'id']
    ordering       = ['-visited_at']
    date_hierarchy = 'visited_at'

    change_list_template = 'admin/pagevisit_change_list.html'

    def get_urls(self):
        urls = super().get_urls()
        return [
            path('analytics/', self.admin_site.admin_view(self.analytics_view),
                 name='core_pagevisit_analytics'),
        ] + urls

    def analytics_view(self, request):
        now   = timezone.now()
        today = now.date()

        total      = PageVisit.objects.count()
        today_ct   = PageVisit.objects.filter(visited_at__date=today).count()
        unique_ips = PageVisit.objects.values('ip_address').distinct().count()
        week_ct    = PageVisit.objects.filter(visited_at__gte=now - timedelta(days=7)).count()

        device_stats  = (PageVisit.objects
                         .values('device_type')
                         .annotate(count=Count('id'))
                         .order_by('-count'))
        browser_stats = (PageVisit.objects
                         .exclude(browser='')
                         .values('browser')
                         .annotate(count=Count('id'))
                         .order_by('-count')[:10])
        os_stats      = (PageVisit.objects
                         .exclude(os='')
                         .values('os')
                         .annotate(count=Count('id'))
                         .order_by('-count')[:10])

        daily = []
        for i in range(13, -1, -1):
            day = today - timedelta(days=i)
            daily.append({
                'label': day.strftime('%b %d'),
                'count': PageVisit.objects.filter(visited_at__date=day).count(),
            })

        recent = PageVisit.objects.order_by('-visited_at')[:100]

        ctx = {
            **self.admin_site.each_context(request),
            'title':         'Visitor Analytics',
            'total':         total,
            'today_ct':      today_ct,
            'unique_ips':    unique_ips,
            'week_ct':       week_ct,
            'device_stats':  device_stats,
            'browser_stats': browser_stats,
            'os_stats':      os_stats,
            'daily':         daily,
            'max_daily':     max((d['count'] for d in daily), default=1),
            'recent':        recent,
        }
        return render(request, 'admin/visitor_analytics.html', ctx)
