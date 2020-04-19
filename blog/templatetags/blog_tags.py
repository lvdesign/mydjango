from django.db.models import Count
from django import template
from ..models import Post

from django.utils.safestring import mark_safe
import markdown

#
register = template.Library()

@register.simple_tag
def total_posts():
    '''
    Let's start by creating a simple tag to retrieve the total posts published on the blog.
    '''
    return Post.published.count()


@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    '''
    Using an inclusion tag, you can render
    a template with context variables returned by your template tag
    The template tag is called, passing the number of posts to display, and the template
    is rendered in place with the given context.
    '''
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts':latest_posts }


@register.simple_tag
def get_most_commented_posts(count=5):
    '''
    You use the Count aggregation function to store the number of comments in the computed field total_comments for each Post object. You order the QuerySet by the computed field in descending order. You also provide an optional count variable to limit the total number of objects returned
    '''
    return Post.published.annotate(total_comments= Count('comments')).order_by('-total_comments')[:count]


@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))