from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=250)
    pub_date = models.DateTimeField()
    body_text =models.TextField()
    image = models.ImageField(upload_to="images/")

    def summary(self):
        if len(self.body_text) > 99:
            return self.body_text[:100]+"..."
        else:
            return self.body_text[:100]

    def pub_date_modified(self):
        return self.pub_date.strftime("%Y-%m-%d")

    def __str__(self):
        return self.title
