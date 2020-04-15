from django.urls import path
from . import views

app_name = 'blog'

'''
Creating a urls.py file for each application is the best way to
make your applications reusable by other projects.
'''

urlpatterns = [
    # post views
    # You use path converters, such as <int:year>,

    # path('', views.post_list, name='post_list'),
    
    path('', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
]