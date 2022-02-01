from unittest import TestCase

from store.models import Book
from store.serializers import BookSerializer


class BookSerializerTestCase(TestCase):

    def test_ok(self):
        book_1 = Book.objects.create(
            name='test-book',
            price=893
        )
        book_2 = Book.objects.create(
            name='test-book1',
            price=593
        )
        data = BookSerializer([book_1, book_2], many=True).data
        expected_data = [
            {
                'id': book_1.id,
                'name': 'test-book',
                'price': '893.00'
            },
            {
                'id': book_2.id,
                'name': 'test-book1',
                'price': '593.00'
            },
        ]
        self.assertEqual(expected_data, data)