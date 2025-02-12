from rest_framework.exceptions import ValidationError
from  rest_framework import serializers
from books.models import Books

# class BooksSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Books
#         fields = '__all__' #or ['id', 'title', 'subtitle', 'author', 'isbn', 'price']


# class BooksSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=200)
#     subtitle = serializers.CharField(max_length=200)
#     author = serializers.CharField(max_length=200)
#     isbn = serializers.CharField(max_length=13)
#     price = serializers.DecimalField(max_digits=100, decimal_places=2)

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'

    def validate(self, data):
        title = data.get('title')
        author = data.get('author')

        # Check if title consists only of letters and spaces
        if title and not title.replace(" ", "").isalpha():
            raise ValidationError({
                "status": False,
                "message": "Kitobning Sarlavhasi harflardan iborat bo'lishi kerak!"
            })

        # Check if title and author combination is unique
        if title and author:
            instance = getattr(self, 'instance', None)  # Handle update scenario
            query = Books.objects.filter(title=title, author=author)
            if instance:
                query = query.exclude(id=instance.id)

            if query.exists():
                raise ValidationError({
                    "status": False,
                    "message": "Bunday kitob mavjud!"
                })
        return data

    def validate_author(self, value):
        # Ensure author name consists only of letters and spaces
        if not value.replace(" ", "").isalpha():
            raise ValidationError({
                "status": False,
                "message": "Kitobning muallifi harflardan iborat bo'lishi kerak!"
            })
        return value

    def validate_price(self,  price):
        if price < 0:
            raise ValidationError({
                "status": False,
                "message": "Narxi noto'g'ri kiritilgan!"
            })
