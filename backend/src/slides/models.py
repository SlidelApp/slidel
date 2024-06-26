from django.db import models


# Create your models here.
class Slides(models.Model):
    title = models.CharField(max_length=100)
    uploaded_file = models.FileField(upload_to="slides/")
    user = models.ForeignKey("account.CustomUser", on_delete=models.CASCADE)

    def __str__(self):
        return self.title
