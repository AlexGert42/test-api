from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from store.models import Book
from store.serializers import BookSerializer


class BooksApiTestCase(APITestCase):

    def setUp(self):
        self.book_1 = Book.objects.create(
            name='test-book',
            price=893,
            author_name='author_'
        )
        self.book_2 = Book.objects.create(
            name='test-book1',
            price=593,
            author_name='author_1'
        )
        self.book_3 = Book.objects.create(
            name='test-book2',
            price=300,
            author_name='author_2'
        )

    def test_get(self):
        url = reverse('book-list')
        response = self.client.get(url)
        serializer_data = BookSerializer([self.book_1, self.book_2, self.book_3], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)


    def test_filter(self):
        pass