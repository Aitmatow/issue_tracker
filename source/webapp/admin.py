from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from accounts.models import Profile, Teams
# Register your models here.
from webapp.models import Issue, Statuses, Tips, Projects


class IssueAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'description', 'status', 'tip', 'create_date']
    list_filter = ['status', 'tip']
    list_display_links = ['pk']
    search_fields = ['title']
    exclude = []
    readonly_fields = ['create_date']


class ProfileInline(admin.StackedInline):
    model = Profile
    fields = ['birth_date', 'avatar','git_repo']


class ProfileAdmin(UserAdmin):
    inlines = [ProfileInline]




admin.site.register(Issue, IssueAdmin)
admin.site.register(Statuses)
admin.site.register(Tips)
admin.site.register(Projects)
admin.site.register(Profile)
admin.site.unregister(User)
admin.site.register(User, ProfileAdmin)
admin.site.register(Teams)