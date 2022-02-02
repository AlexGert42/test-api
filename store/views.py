from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Book
from .serializers import BookSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, OrderingFilter]
    permission_classes = [IsAuthenticated]
    filter_fields = ['price', 'author_name']
    search_fields = ['name', 'author_name']
    ordering_fields = ['price', 'author_name']