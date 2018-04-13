from django.db import models 


class MessageForm(models.Model):
    first_name = models.CharField(max_length=400)
    email = models.CharField(max_length=20)
    message = models.CharField(max_length=800)


    def __str__(self):
        return self.first_name

class Subscription(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email


class Blog(models.Model):
    image = models.FileField(upload_to='documents/')
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=200000)
    upvote = models.BooleanField(default=False)
    objects = models.Manager()

    def __str__(self):
        return self.title

