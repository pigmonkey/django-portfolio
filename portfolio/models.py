from django.db import models
from sorl.thumbnail import ImageField

class Type(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30, unique=True)
    description = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name
    
    @models.permalink
    def get_absolute_url(self):
        return ('portfolio.views.projects_by_type', [str(self.slug)])


class Role(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name
    
    @models.permalink
    def get_absolute_url(self):
        return ('portfolio.views.projects_by_role', [str(self.slug)])

class Skill(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name
    
    @models.permalink
    def get_absolute_url(self):
        return ('portfolio.views.projects_by_skill', [str(self.slug)])

class Client(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField(blank=True)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    url = models.URLField(blank=True, null=True)
    short_description = models.TextField()
    description = models.TextField()
    completion_date = models.DateField()
    image = models.ImageField(upload_to='images/portfolio', blank=True)
    type = models.ForeignKey(Type)
    role = models.ManyToManyField(Role)
    skills = models.ManyToManyField(Skill)
    client = models.ForeignKey(Client)
    public = models.BooleanField(default=True)

    class Meta:
        ordering = ['-completion_date']

    def __unicode__(self):
        return self.name
    
    @models.permalink
    def get_absolute_url(self):
        return ('portfolio.views.project_detail', [str(self.slug)])
