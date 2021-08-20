from django.urls import path
from rest_framework import urlpatterns
from .views import PostList, PostDetail, PostListDetailFilter, EditPost, DeletePost, CreatePost, AdminPostDetail
from rest_framework.routers import DefaultRouter

app_name = 'blog_api'

# router = DefaultRouter()
# router.register('', PostList, basename='post')
# urlpatterns = router.urls


urlpatterns = [
    path('post/', PostDetail.as_view(), name='detailcreate'),
    path('search/', PostListDetailFilter.as_view(), name='postsearch'),
    path('', PostList.as_view(), name='listcreate'),
    # Admin urls
    path('admin/create/', CreatePost.as_view(), name='createpost'),
    path('admin/edit/postdetail/<int:pk>/',
         AdminPostDetail.as_view(), name='admindetailpost'),
    path('admin/delete/<int:pk>/', DeletePost.as_view(), name='deletpost'),
    path('admin/edit/<int:pk>/', EditPost.as_view(), name='editpost'),
]
