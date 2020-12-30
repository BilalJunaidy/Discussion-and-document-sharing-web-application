from django.db import models
from django.contrib.auth.models import User 
from PIL import Image

# Create your models here.


# So in this situation, we are basically creating a Proxy model (as explained in the official django documentation) to relate our Profile and the User model. 
# There is no real need for us to have a seperate django app to place this Profile proxy model. 
# In essence here, we are still using the default User model of Django, and then storing additional fields into this Profile proxy model. 
# So why use this approach and not substitute a custom user model?

# 1. If you want to use username as the default mechanisms as the unique token for identification, then you can use Django's 
    #  default User model.

# 2. I can only use the LoginView and the LogoutView if I am using Django's default User model. However, this is not really that big of a deal
#    since there are numerous ways for us to authenticate and login a Custom User model within Django. 
#    For example, we have at our disposal the AuthenticateForm, as well as authenticate() and login() methods. 

# 3. One important use case of using the Django's default User model is in the instance that you have multiple apps each in which the Profile proxy model 
# has different requirements. So for example, you can use Django's default User model simply for the purposes of authentication, and then we can 
# have seperate Profile proxy models (one for each django app). 
# The reason why we would have seperate apps is because if each of these profile proxy models are different in terms of their attributes.



# On the contrary, why would you actually not use this proxy model approach and actually substitute a custom user model?
# 1. In this proxy model, if there is a User object created, then there is no feature that auto-creates a Profile proxy model object. 
#    We have to use the "django.db.models.signals.post_save" method to perform this action. 
#    So if you don't want to use signals, then substitute the default Django User model with a custom User model. 

# 2. If we want to access attributes of the Profile model using the User object, we will do something like the following:
#    myuser = User.objects.all().first()
#    url = myuser.profile.image.url

#    The issue with this approach is that in the background, do access these related model (i.e. the Profile proxy model)'s fields,
#    django had to perform join and/or additional queries, which will make the process slightly slower. 
#    So if effeciency is your end objective, then maybe consider creating a Custom User model.

# 3. Django's default User model uses the username as the unique identification token for authenticating purposes. 
    #  If the requirements for your project is that you need to use (lets say the email address) to act as the 
    #  unique identification token for authenticating purposes, then you need to substitute a custom User model instead of using 
    #  the default django user model. 

# 4. Although, the UserCreationForm can not be directly used if we were to use a Custom User model, it can be easily inherited from to 
#    create a CustomUserCreationForm. 
#    Here is an example:

#    from django.contrib.auth.forms import UserCreationForm
#     from myapp.models import CustomUser

#     class CustomUserCreationForm(UserCreationForm):

#         class Meta(UserCreationForm.Meta):
#             model = CustomUser
#             fields = UserCreationForm.Meta.fields + ('custom_field',)

#    Here is the reference for this example:
#    https://docs.djangoproject.com/en/3.1/topics/auth/customizing/#custom-users-and-the-built-in-auth-forms

# 5. Even if we substitute Django's default User model with our own Custom User model, we still do have access to loads of 
#    Django built in forms and views.
#    If we don't have access to these directly, then we can easily extend these to match our requirements.  



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(default = 'default.png', upload_to = 'Profile_Pics')

    def __str__(self):
        return f"{self.user.username} Profile"

    def save(self):
        super().save()

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

