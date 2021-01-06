from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
from . import views


# So why do we need to use the .as_view() method when using class-based views? Here is why:

# Because Django’s URL resolver expects to send the request and associated arguments to a callable function, not a class, 
# class-based views have an as_view() class method which returns a function that can be called when a request arrives for a URL 
# matching the associated pattern. The function creates an instance of the class, calls setup() to initialize its attributes, 
# and then calls its dispatch() method. dispatch looks at the request to determine whether it is a GET, POST, etc, 
# and relays the request to a matching method if one is defined, or raises HttpResponseNotAllowed if not.

urlpatterns = [
    # path('', views.home, name='blog-home'),
    path('', PostListView.as_view(), name='blog-home'),
    # "pk" is the default name of the primary key field name used by django to filter the queryset. 
    # If you want to name it something else, you will have to override the following attribute in the class context: 
    # pk_url_kwarg
    # .....Having said this, there is really no need in doing this tbh, so just stick to the default of pk.

    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name = 'post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name = 'post-delete'),
    path('about/', views.about, name='blog-about'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts')

]