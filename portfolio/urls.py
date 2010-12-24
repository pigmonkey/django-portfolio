from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.generic import list_detail
from portfolio import views
from models import Type, Role, Skill, Project

admin.autodiscover()

types = {
    'queryset': Type.objects.all(),
    'template_object_name': 'type',
}

roles = {
    'queryset': Role.objects.all(),
    'template_object_name': 'role',
}

skills = {
    'queryset': Skill.objects.all(),
    'template_object_name': 'skill',
}

projects = {
    'queryset': Project.objects.filter(public=True),
    'template_object_name': 'project',
    'template_name': 'portfolio/all_projects.html',
}

urlpatterns = patterns('',
    (r'^$', list_detail.object_list, projects, "projects_view"),
    (r'^types/$', list_detail.object_list, types, "types_view"),
    (r'^type/([-\w]+)/$', views.projects_by_type),
    (r'^roles/$', list_detail.object_list, roles, "roles_view"),
    (r'^role/(?P<role_slug>[-\w]+)/$', views.projects_by_role, {'type_slug': 'all'}),
    (r'^skills/$', list_detail.object_list, skills, "skills_view"),
    (r'^skill/([-\w]+)/$', views.projects_by_skill),
    (r'^(?P<type_slug>[-\w]+)/(?P<role_slug>[-\w]+)/$', views.projects_by_role),
    url(r'^(?P<slug>[-\w]+)/$', views.project_detail,),
)
