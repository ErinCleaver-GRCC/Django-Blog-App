from django.shortcuts import render
from django.utils import timezone
from .models import Post



# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    list_of_posts = {
        'posts': posts
    }
    return render(request, 'blog/post_list.html', list_of_posts)