import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status

from rest_framework.test import APITestCase

from store.models import Book
from store.serializers import BookSerializer


class BooksApiTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(username='test_user')
        self.book_1 = Book.objects.create(
            name='test-book',
            price=893,
            author_name='author_',
            owner=self.user
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
        self.client.force_login(self.user)
        response = self.client.get(url)
        serializer_data = BookSerializer([self.book_1, self.book_2, self.book_3], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_filter(self):
        pass

    def test_create(self):
        url = reverse('book-list')
        data = {
            "name": "Harry Potter",
            "price": 1000,
            "author_name": "Joanne Rowling"
        }
        json_data = json.dumps(data)
        self.client.force_login(self.user)
        response = self.client.post(url, data=json_data, content_type='application/json')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)

    def test_update(self):
        url = reverse('book-detail', args=(self.book_1.id,))

        data = {
            "name": "test-book",
            "price": 1000,
            "author_name": "author_"
        }
        json_data = json.dumps(data)
        self.client.force_login(self.user)
        response = self.client.put(url, data=json_data, content_type='application/json')
        print(response.data)
        self.book_1.refresh_from_db()
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_(self):
        url = reverse('userbookrelation-detail')

        data = {
            "like": True
        }
        json_data = json.dumps(self.user)
        self.client.force_login(self.user)

        resource = self.client.get(url)
        serializer_data = BookSerializer([])
