from django.contrib import admin
from accounts.models import Profile
# Register your models here.
from webapp.models import Issue, Statuses, Tips, Projects


class IssueAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'description', 'status', 'tip', 'create_date']
    list_filter = ['status', 'tip']
    list_display_links = ['pk']
    search_fields = ['title']
    exclude = []
    readonly_fields = ['create_date']

admin.site.register(Issue, IssueAdmin)
admin.site.register(Statuses)
admin.site.register(Tips)
admin.site.register(Projects)
admin.site.register(Profile)