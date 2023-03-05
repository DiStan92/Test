
from rest_framework import permissions
from rest_framework.generics import ListAPIView

from .models import Article
from .serializers import ArticleSerializer


class ArticleAPIView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.AllowAny]
