from django.db.models import Q

from Post.models import Post, Comment, Reaction, Picture
from .serializers import PostSerializer, CommentSerializer, ReactionSerializer, PictureSerializer
from .permissions import IsPostOwnerOrReadOnly, IsReactionOwnerOrReadOnly, IsOwnerOrReadOnly
from rest_framework import mixins, generics, permissions


class CommentAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = CommentSerializer
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get_queryset(self):
        qs = Comment.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query)
            ).distinct()
        return qs

    def perform_create(self, serializer):
        serializer.save(comment_owner=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class CommentRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsOwnerOrReadOnly
    ]


class ReactionAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = ReactionSerializer
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get_queryset(self):
        qs = Reaction.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query)
            ).distinct()
        return qs

    def perform_create(self, serializer):
        serializer.save(reaction_owner=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class ReactionRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    queryset = Reaction.objects.all()
    serializer_class = ReactionSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsReactionOwnerOrReadOnly
    ]


class PostAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = PostSerializer
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get_queryset(self):
        qs = Post.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query)
            ).distinct()
        return qs

    def perform_create(self, serializer):
        serializer.save(post_owner=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class PostRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsPostOwnerOrReadOnly
    ]


class PictureAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = PictureSerializer
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get_queryset(self):
        qs = Picture.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query)
            ).distinct()
        return qs

    def perform_create(self, serializer):
        serializer.save(post_owner=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class PictureRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer
    permission_classes = [
        permissions.IsAuthenticated,
    ]
