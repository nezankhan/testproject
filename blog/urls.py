from django.urls import path
from . import views
from . views import PostListView, PostDetailView


#to use class based view instead of function based view, we import our view
#PLease note that PostListView will look for template with the following path.name
# app/model_viewtype.html in our case it would be blog/post_list.html
# we can change our template name or we can specify which template to use

urlpatterns = [
    path('', PostListView.as_view(),name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(),name='post-detail'),
    path('about/', views.about,name='blog-about'),
]

