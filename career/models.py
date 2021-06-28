from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Career(models.Model):
    owner = models.ForeignKey("auth.User", verbose_name="Owner", on_delete= models.CASCADE)
    firm = models.CharField(verbose_name="Firm", max_length=80)
    advert_title = models.CharField(verbose_name="Title", max_length=80)
    content = RichTextField()
    advert_date =  models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.advert_title
