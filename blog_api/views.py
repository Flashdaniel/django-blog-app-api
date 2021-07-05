from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, SAFE_METHODS, BasePermission

from blog.models import Post
from .serializers import PostSerializer


class PostUserWritePermission(BasePermission):
    message = "Editing Posts is restricted to the author only."

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True

        return obj.author == request.user


class PostList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):
    permission_classes = [PostUserWritePermission]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
