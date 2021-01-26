from django.urls import path

from .views import (
  IndexView, 
  PostDetailView,
  CategoryListView,
  TagListView,
  CategoryPostView,
  TagPostView,
  SearchPostView,
)

app_name = 'manual'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('tags/', TagListView.as_view(), name='tag_list'),
    path('category/<str:category_slug>/',
        CategoryPostView.as_view(), name='category_post'),
    path('tag/<str:tag_slug>/', TagPostView.as_view(), name='tag_post'),
    path('search/', SearchPostView.as_view(), name='search_post'),
]