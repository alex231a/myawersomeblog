from django.db import models


class Post(models.Model):
    blog_title = models.CharField(max_length=50)
    blog_date = models.DateTimeField()
    blog_text = models.TextField()
    blog_image = models.ImageField(upload_to='blog_images/')

    def get_summary(self):
        return self.blog_text[:70]

    def __str__(self):
        return self.blog_title
