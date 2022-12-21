from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Project(models.Model):
    project_title = models.CharField(_("Project Title"), max_length=100)
    project_description = models.TextField(_("Project Description"))
    project_technology = models.CharField(_("Technology Used"), max_length=20)
    project_image = models.FilePathField(_("Project Image"), path="/img")

    def __str__(self):
        return self.project_title

    class Meta:
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")
