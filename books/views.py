from logging import raiseExceptions
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from books.models import Books
from rest_framework import generics, status
from books.serializers import BooksSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

#Class Based
# class BooksListApiView(generics.ListAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BooksSerializer

class BooksListApiView(APIView):
    def get(self, request):
        books = Books.objects.all()
        serializer_data = BooksSerializer(books, many=True).data
        data = {
            "status": f"Returned {len(books)} books",
            "books": serializer_data
        }
        return Response(data)

# class BookDetailApiView(generics.RetrieveAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BooksSerializer


class BookDetailApiView(APIView):
    def get(self, request, pk):
        try:
            book = Books.objects.get(pk=pk)
            serializer_data = BooksSerializer(book).data
            data = {
                "status": f"Book: {book.title}",
                "book": serializer_data
            }
            return Response(data, status=status.HTTP_200_OK)
        except Exception:
            return Response({
                "status": "error(False)",
                "message": "Book not found",
            }, status=status.HTTP_404_NOT_FOUND)



# class BookDeleteApiView(generics.DestroyAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BooksSerializer


class BookDeleteApiView(APIView):
    def delete(self, request, pk):
        try:
            book = get_object_or_404(Books, pk=pk)
            book.delete()
            data = {
                "status": True,
                "message": "Book deleted"
            }
            return Response(data, status=status.HTTP_200_OK)
        except Exception:
            return Response({
                "status": False,
                "message": "Book not found",
            }, status=status.HTTP_404_NOT_FOUND)

# class BookUpdateApiView(generics.UpdateAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BooksSerializer


class BookUpdateApiView(APIView):
    def put(self, request, pk):
        book = get_object_or_404(Books, pk=pk)
        data = request.data
        serializer = BooksSerializer(instance=book, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            book_saved = serializer.save()
        return Response(
            {
                "status": 'Book updated',
                "book": f"Book: '{book_saved.title}' has been updated"
            }
        )

# class BookCreateApiView(generics.CreateAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BooksSerializer

class BookCreateApiView(APIView):
    def post(self, request):
        serializer = BooksSerializer(data=request.data)  # Создаём сериализатор с входными данными

        if serializer.is_valid(
                raise_exception=True):  # Проверяем валидность, сразу выбрасываем ошибку 400, если невалидно
            book = serializer.save()  # Сохраняем книгу
            return Response({
                "status": "Book has been created",
                "book": serializer.data  # Отправляем данные созданной книги
            }, status=201)  # 201 Created

        # Этот return никогда не выполнится из-за raise_exception=True, но оставлен для читаемости кода
        return Response(serializer.errors, status=400)


class BooksListCreateApiView(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer


class BooksUpdateDeleteApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer


#For CRUD operations
class BookViewSet(ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            return self.queryset
        return self.queryset.filter(pk=pk)

#Function Based
@api_view(['GET'])
def books_list_view(request, *args, **kwargs):
    books = Books.objects.all()
    serializer = BooksSerializer(books, many=True)
    return Response(serializer.data)