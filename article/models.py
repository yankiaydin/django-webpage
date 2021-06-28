from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Article(models.Model):
    title = models.CharField(verbose_name="Title", max_length=100)
    date = models.DateTimeField(auto_now_add=True, verbose_name="Date")
    author = models.ForeignKey("auth.User", verbose_name="Author", on_delete= models.CASCADE)
    content = RichTextField()
    article_image = models.ImageField(blank=True, verbose_name="Article Image")
    def __str__(self):
        return self.title

class Comment(models.Model):
    commenter = models.ForeignKey("auth.User", on_delete= models.CASCADE)
    comment_date = models.DateTimeField(auto_now_add=True)
    comment_content = models.CharField(verbose_name="Content", max_length=100, blank=True)
    comment_to = models.ForeignKey(Article,on_delete=models.CASCADE)
    def __str__(self):
        return "%s %s" % (self.commenter, self.comment_to)
