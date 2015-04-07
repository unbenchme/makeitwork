from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

#Category tracks broad skill-type categories (i.e. Python, Java, Tax, Excel, etc.)
class Category(models.Model):
    #username = models.ForeignKey(User, related_name='category_created_by')                                   #Tracks who created what category
    category_name = models.CharField(max_length=100, default = "A Category")
    timestamp = models.DateTimeField(auto_now_add=True          )                  #Timestamp of when category created
    def __unicode__(self):
        return self.category_name

#Requests is a request for help by a user
class Request(models.Model):
    #created_by = models.ForeignKey(User, related_name='request_created_by')                      #Username from contrib.auth
    name = models.CharField(max_length=100, default = "A Project")
    time_in_hours = models.DecimalField(max_digits=4,decimal_places=2)          #Time request will take in hours
    timestamp = models.DateTimeField(auto_now_add=True)                                  #Timestamp of request
    category_name = models.ForeignKey(Category)                                 #Category of request from Category Class
    number_of_people = models.DecimalField(max_digits=2,decimal_places=0)       #Number of people requested
    def __unicode__(self):
        return self.name

# #Available identifies whether a user is available or not
class Available(models.Model):
    username = models.ForeignKey(User, related_name='available_username', default=User.pk)                      #Username from contrib.auth
    is_available = models.BooleanField(default=None)
    def __unicode__(self):
        return self.available_username, self.is_available

# #RequestAccept identifies who is currently accepting what request
class RequestAccept(models.Model):
    username = models.ForeignKey(User, related_name='request_accept_username', default=User.pk)                      #Username from contrib.auth
    request_id = models.ForeignKey(Request)                                    #Request from request class
    def __unicode__(self):
        return self.username, self.request_id
