from django.urls import path
from . import views

app_name = 'blog'

url_cut = 'category/<slug:category_slug>/'

urlpatterns = [
    path('posts/<int:id>/', views.post_detail, name='detail'),
    path(url_cut, views.category_posts, name='category_posts'),
    path('', views.index, name='index')
]