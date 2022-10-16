from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView

# Create your views here.
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request,'blog/home.html',context)


#Class based view

class PostListView(ListView):
    #we need to reference our model that will be used to create the view in this case it will be post
    model = Post
    # app/model_viewtype.html in our case it would be blog/post_list.html
    template_name = 'blog/home.html'
    #we also need to name our variable that our html will loop through
    context_object_name = 'posts'
    ordering= ['-date_posted']

class PostDetailView(DetailView):
    #we need to reference our model that will be used to create the view in this case it will be post
    model = Post

def about(request):
    return render(request,'blog/about.html',{'title':'title'})


