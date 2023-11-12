from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


class PostList(ListView):
    model = Post
    ordering = '-pk'

class PostDetail(DetailView):
    model = Post

# Create your views here.
# Class PostDetail(DetailView):
#     model = Post
#    def landing(request):
#    return render(
#        request,
#        'single_pages/landing.html',
#    )

def single_post_page(request, pk):

    post = Post.objects.get(pk=pk)

    return render(
        request,
        'blog/post_detail.html',
        {
            'post':post,
        }
    )

def index(request):
    return render(
        request,
        'blog/post_list.html',
    )