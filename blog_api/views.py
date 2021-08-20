from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, SAFE_METHODS, BasePermission, IsAuthenticated
from rest_framework.response import Response
from rest_framework import filters

from blog.models import Post
from .serializers import PostSerializer
from rest_framework.parsers import MultiPartParser, FormParser


class PostUserWritePermission(BasePermission):
    message = "Editing Posts is restricted to the author only."

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True

        return obj.author == request.user


# class PostList(viewsets.ModelViewSet):
#     permission_classes = [PostUserWritePermission]
#     serializer_class = PostSerializer

#     def get_object(self, queryset=None, **kwargs):
#         item = self.kwargs.get('pk')
#         return generics.get_object_or_404(Post, slug=item)

#     def get_queryset(self):
#         user = self.request.user
#         queryset = Post.objects.filter(author=user)
#         return queryset

# class PostList(viewsets.ViewSet):
#     queryset = Post.postobjects.all()
#     permission_classes = [IsAuthenticatedOrReadOnly]

#     def list(self, request):
#         serializer = PostSerializer(self.queryset, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         post = generics.get_object_or_404(self.queryset, pk=pk)
#         serializer = PostSerializer(post)
#         return Response(serializer.data)

class PostList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(author=user)


class PostDetail(generics.RetrieveAPIView):
    # permission_classes = [PostUserWritePermission]
    serializer_class = PostSerializer

    # def get_queryset(self):
    #     slug = self.kwargs.get('pk')
    #     print(slug)
    #     return Post.objects.filter(slug=slug)

    def get_object(self, queryset=None, **kwargs):
        item = self.request.query_params.get('slug', None)
        return generics.get_object_or_404(Post, slug=item)


class CreatePost(generics.CreateAPIView):
    queryset = Post.objects.all()
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer


class AdminPostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer


class EditPost(generics.UpdateAPIView):
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer


class DeletePost(generics.DestroyAPIView):
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer


class PostListDetailFilter(generics.ListAPIView):
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^slug']
