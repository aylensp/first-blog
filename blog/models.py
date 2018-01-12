from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    autor = models.ForeignKey('auth.User')
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    autor = models.CharField(max_length=200)
    texto = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.texto

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)
