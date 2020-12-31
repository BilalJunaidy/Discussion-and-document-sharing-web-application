# The User model here is the sender 

from django.db.models.signals import post_save
from django.contrib.auth.models import User 

# The receiver is going to get this signal from the User model when we the post_save signal is trigerred on the by the User model    
from django.dispatch import receiver 
from .models import Profile

# The reason why we assign a model to the sender below in the decorator is because we only want the create_profile and 
# save_profile functions to be executed ONLY when the User object's save method has been fully executed (hence the signal we are using is called 
# "post_save").

# post_save below is a signal instance. 
# If you want to register multiple signals, then we can have the first argument to the decorator a list/tuple of signal instances we would like to register.

# Now this is important to note. I do recognize that you very much enjoy event driven programming (coz of VBA and JavaScript), 
# and therefore, it might seem like a good idea to use signals more often in Django since they are essentially very similar to event driven programming. 
# However, you need to be very careful before deciding to use signals. 
# The following are good rules to follow in making this determination:
# a. If you have two apps, and one app wants to trigger behaviour in an app it already knows about, don’t use signals
# b. Only use signals to avoid introducing circular dependencies. You don't want to be in a situation in which lets say there are two apps, and both of them are 
# dependent on each other (circular dependencies) and therefore, this would be a good use case to use signals since you can then possibly remove the circular depencdency
# and help ensure that our apps have single flow.


The following are good resources for understanding signals:
1. https://simpleisbetterthancomplex.com/tutorial/2016/07/28/how-to-create-django-signals.html
2. https://medium.com/@ksarthak4ever/django-signals-b20a4152a27b
3. https://stackabuse.com/using-django-signals-to-simplify-and-decouple-code/


@receiver(post_save, sender = User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance)
    

@receiver(post_save, sender = User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()