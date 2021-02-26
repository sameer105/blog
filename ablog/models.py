from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.utils import timezone
from django.urls import reverse
from ckeditor.fields import RichTextField
#from pip._vendor.certifi.__main__ import args

class Category(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
       # return reverse('details', args(str(self.id)))
        return reverse('home')




class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(max_length=255, null=True, blank= True)
    website_url = models.CharField(max_length=255, null=True, blank=True)
    facebook_url = models.CharField(max_length=255, null=True, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)
    pinterest_url = models.CharField(max_length=255, null=True, blank=True)


    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('home')



class Post(models.Model):
    title = models.CharField(max_length=255)
    header_image = models.ImageField(null=True, blank= True, upload_to="images/profile/")
    title_tag = models.CharField(max_length=255, default="My Blog.....")
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    # body = models.TextField()
    category = models.CharField(max_length=255, default='coding')
    snippet = models.CharField(max_length=255)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    likes = models.ManyToManyField(User, related_name='blog_post')

    def total_likes(self):
        return self.likes.count()

    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
       # return reverse('details', args(str(self.id)))
        return reverse('home')

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name= "comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)

