from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # 내가 직렬화할 모델과, 필드를 Meta 클래스에 명시
        model = Book
        fields = [
            'image_URL',
            'author',
            'title',
            'desc',
            'edition',
            'isbn',
            'rating'
            ]
  