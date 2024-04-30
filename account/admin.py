from django.contrib import admin

from account.models import AgentUser
# Register your models here.

class AgentUserAdmin(admin.ModelAdmin):
    list_display = ['username',]




admin.site.register(AgentUser, AgentUserAdmin)
