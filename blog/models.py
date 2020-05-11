from django.db import models

from django.utils import timezone

from django.contrib.auth.models import User
from django.urls import reverse

from taggit.managers import TaggableManager


# Create your models here.

# A Custom Manager Creating model managers p.25
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status='published')
        #return super().get_queryset().filter(status='published')

# 
class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField( max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User,on_delete=models.CASCADE, related_name='blog_posts')

    body= models.TextField()
    image = models.ImageField(upload_to='images/%Y/%m/%d', blank=True)

    publish= models.DateTimeField(default=timezone.now)
    created= models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    tags = TaggableManager()

    # Manager    
    objects = models.Manager() #default manager
    published = PublishedManager() #Our custom manager

    class Meta:
        ordering = ('-publish',)
    
    def __str__(self):
        return self.title


    # Urls
    def get_absolute_url(self):
        return reverse('blog:post_detail',args=[self.publish.year,self.publish.month,   self.publish.day,self.slug])


# Comment system
class Comment(models.Model):
    '''
    This is your Comment model. It contains a ForeignKey to associate a comment with a
    single post. This many-to-one relationship is defined in the Comment model because
    each comment will be made on one post, and each post may have multiple comments.

    You have included an active Boolean field that you will use to manually deactivate
    inappropriate comments. You use the created field to sort comments in a
    chronological order by default.
    '''
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)
    
    def __str__(self):
        return f'Comment by {self.name} on { self.post}'

