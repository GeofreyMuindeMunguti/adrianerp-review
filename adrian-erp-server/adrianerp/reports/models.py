from django.db import models

# Create your models here.

class Issues(models.Model):
    # project_name = models.ForeignKey(MainSite, on_delete=models.DO_NOTHING)
    issue = models.CharField(max_length=100)
    issue_image = models.ImageField(upload_to='images/InstallationTeam/issues/%Y/%m/%d/', blank=True, null=True)
    issue_sorted_image = models.ImageField(upload_to='images/InstallationTeam/issues/%Y/%m/%d/', blank=True, null=True)
    closed = models.BooleanField(default=False)
    # posted_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.issue

class Site(models.Model):
    # project_name = models.ManyToManyField(MainSite, blank=True, null=True)
    site_number = models.CharField(max_length=100, unique=True, blank=True, null=True)
    BTS_type = models.CharField(max_length=100, blank=True, null=True)
    site_owner = models.CharField(max_length=100, blank=True, null=True)
    # icon = models.ForeignKey(ProjectIcons, on_delete=models.DO_NOTHING, blank=True, null=True)
    # location = models.ForeignKey(Location, on_delete=models.DO_NOTHING, blank=True, null=True)
    geotech_file = models.FileField(upload_to='files/Project/geotech/%Y/%m/%d/', blank=True, null=True)
    access_letter = models.FileField(upload_to='files/Project/accessletters/%Y/%m/%d/', blank=True, null=True)
    approved_drawing = models.FileField(upload_to='files/Project/approveddrawings/%Y/%m/%d/', blank=True, null=True)
    final_acceptance_cert = models.FileField(upload_to='files/SafaricomTeam/finalcert/%Y/%m/%d/', blank=True, null=True)
    final_acceptance_cert_comment = models.CharField(max_length=100, blank=True, null=True)
    # created_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_name)


