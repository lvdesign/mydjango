from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView

# Create your views here.



class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'

'''
# List des Posts avec une fonction
def post_list(request):
    object_list = Post.published.all()

    paginator = Paginator(object_list,3)
    page = request.GET.get('page')
    try:
        posts= paginator.page(1)
    except PageNotAnInteger:
        # if
        posts = paginator.page(1)
    except EmptyPage: 
        posts = paginator.page(paginator.num_pages) 

    #posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'page': page, 'posts': posts})
'''

# One Post
def post_detail(request, year, month, day, post):
    '''
    when you created the Post model, you added the
    unique_for_date parameter to the slug field. This ensures that there will be only one post with a slug for a
    given date, and thus, you can retrieve single posts using the date and slug.
    '''
    post = get_object_or_404( Post, slug=post, status='published', publish__year =year, publish__month = month, publish__day= day
    )
    return render(request,'blog/post/detail.html', {'post': post})