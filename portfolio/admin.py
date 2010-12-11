from django.contrib import admin
from portfolio.models import *

class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
admin.site.register(Project, ProjectAdmin)

class SkillAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
admin.site.register(Skill, SkillAdmin)

class TypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
admin.site.register(Type, TypeAdmin)

class RoleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
admin.site.register(Role, RoleAdmin)

admin.site.register(ProjectMeta)
admin.site.register(Client)
