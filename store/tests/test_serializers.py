from unittest import TestCase

from store.models import Book
from store.serializers import BookSerializer


class BookSerializerTestCase(TestCase):

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

    def test_ok(self):

        data = BookSerializer([self.book_1, self.book_2], many=True).data
        expected_data = [
            {
                'id': self.book_1.id,
                'name': 'test-book',
                'price': '893.00',
                'author_name': 'author_'
            },
            {
                'id': self.book_2.id,
                'name': 'test-book1',
                'price': '593.00',
                'author_name': 'author_1'
            },
        ]
        self.assertEqual(expected_data, data)