from django.db import models
from django.urls import reverse

class Job(models.Model):
    # Basic Information
    title = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    posted_on = models.DateTimeField(auto_now_add=True)

    # Job Details
    vacancies = models.IntegerField(default=1)
    age_limit = models.CharField(max_length=100, blank=True, null=True)
    eligibility = models.TextField(blank=True, null=True)
    selection_process = models.TextField(blank=True, null=True)
    application_process = models.TextField(blank=True, null=True)
    application_fee = models.CharField(max_length=100, blank=True, null=True)

    # Application Info
    application_deadline = models.DateField()
    application_link = models.URLField()
    description = models.TextField()

    # Extra
    more_information = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.organization}"

    def get_absolute_url(self):
        return reverse("job_detail", args=[str(self.id)])


# New Model for Multiple Images
class JobVacancyImage(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="vacancy_images")
    image = models.ImageField(upload_to="vacancy_images/")  # saved in MEDIA folder
    caption = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"Image for {self.job.title}"
