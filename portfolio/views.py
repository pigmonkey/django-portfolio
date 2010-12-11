from django.shortcuts import get_object_or_404
from django.views.generic import list_detail
from models import Project, Type, Role, Skill

def projects_by_type(request, slug):

    # Look up type (and raise a 404 if it can't be found).
    type = get_object_or_404(Type, slug__iexact=slug)

    # Use the generic object_list view to return the list of projects
    return list_detail.object_list(
        request,
        queryset = Project.objects.filter(type=type),
        template_name = 'portfolio/projects_by_type.html',
        template_object_name = 'project',
        extra_context = {'type': type}
    )

def projects_by_role(request, type_slug, role_slug):

    # Look up role (and raise a 404 if it can't be found).
    role = get_object_or_404(Role, slug__iexact=role_slug)

    context = {'role': role}

    # If a specific type is requested, look up type (and raise a 404 if it can't be found)
    if type_slug != 'all':
        type = get_object_or_404(Type, slug__iexact=type_slug)
        context['type'] = type
    else:
        type = type_slug

    # Filter the queryset for the (type and) role requested
    if type != type_slug:
        queryset = Project.objects.filter(type=type).filter(role=role)
    else:
        queryset = Project.objects.filter(role=role)

    # Use the generic object_list view to return the list of projects
    return list_detail.object_list(
        request,
        queryset,
        template_name = 'portfolio/projects_by_role.html',
        template_object_name = 'project',
        extra_context = context
    )

def projects_by_skill(request, slug):

    # Look up skill (and raise a 404 if it can't be found).
    skill = get_object_or_404(Skill, slug__iexact=slug)

    # Use the generic object_list view to return the list of projects
    return list_detail.object_list(
        request,
        queryset = Project.objects.filter(skills=skill),
        template_name = 'portfolio/projects_by_skill.html',
        template_object_name = 'project',
        extra_context = {'skill': skill}
    )

def project_detail(request, slug):

    # Look up project (and raise a 404 if it can't be found).
    project = get_object_or_404(Project, slug__iexact=slug)

    return list_detail.object_detail(
        request,
        queryset = Project.objects.all(),
        slug = slug,
        slug_field = 'slug',
        template_name = 'portfolio/project_detail.html',
        template_object_name = 'project'
    )
