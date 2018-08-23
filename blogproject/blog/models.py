from django.db import models
from django.utils import timezone
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(to='auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    text = models.TextField()
    create_time = models.DateTimeField(default=timezone.now())
    publish_time = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.publish_time = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved=True)

    def __str__(self):
        return '"{}" by {}'.format(self.title, self.author)

    def get_absolute_url(self):
        return reverse(viewname='post_detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    post = models.ForeignKey(to='blog.Post', related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=300)
    text = models.TextField()
    create_time = models.DateTimeField(default=timezone.now())
    approved = models.BooleanField(default=False)

    def approve(self):
        self.approved = True
        self.save()

    def get_absolute_url(self):
        return reverse(viewname='post_list')
