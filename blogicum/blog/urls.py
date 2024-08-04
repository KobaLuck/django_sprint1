from django.urls import path
from blog.views import category_posts, index, post_detail

app_name = 'blog'

url_cut = 'category/<slug:category_slug>/'

urlpatterns = [
    path('posts/<int:id>/', post_detail, name='post_detail'),
    path(url_cut, category_posts, name='category_posts'),
    path('', index, name='index')
]
