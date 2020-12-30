from django.db import models
from django.utils import timezone
# The following represents Django's default User model.
# Since we are using the default, we don't have to update the AUTH_USER_MODEL in our settings.py file 
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    # The on_delete = models.CASCADE basically is telling Django that if the object represented by the foreign key 
    # is deleted, then Django should also delete all associated Post objects from our database as well. 
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.title}"
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs = {'pk':self.pk})
