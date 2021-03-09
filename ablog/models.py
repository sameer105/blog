from django.conf import settings
from django.db import models
# from django.contrib.auth.models importSSS User
# Create your models here.
from django.utils import timezone
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.core.mail import send_mail
#from pip._vendor.certifi.__main__ import args

class Category(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
       # return reverse('details', args(str(self.id)))
        return reverse('home')

class CustUser(models.Model):
    username = models.CharField(max_length=255, null=True)
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)
    password1 = models.CharField(max_length=255, null=True)
    password2 = models.CharField(max_length=255, null=True)
    is_staff = models.BooleanField
    is_active = models.BooleanField
    is_superuser = models.BooleanField
    # date_joined = models.DateTimeField(auto_now_add=True,blank=True,null=True)


    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        send_mail(
            'Registration Alert!!!!',
            'message',
            settings.EMAIL_HOST_USER,
            [self.email],
        )
        super(CustUser, self).save(*args, **kwargs)



class Profile(models.Model):
    user = models.OneToOneField(CustUser, null=True, on_delete=models.CASCADE)
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
    
    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)



class Post(models.Model):
    title = models.CharField(max_length=255)
    header_image = models.ImageField(null=True, blank= True, upload_to="images/profile/")
    title_tag = models.CharField(max_length=255, default="My Blog.....")
    author = models.ForeignKey(CustUser,on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    # body = models.TextField()
    category = models.CharField(max_length=255, default='coding')
    snippet = models.CharField(max_length=255)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    likes = models.ManyToManyField(CustUser, related_name='blog_post')

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

