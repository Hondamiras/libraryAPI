from django.urls import path
from books.views import BooksListApiView, books_list_view, \
    BookDetailApiView, BookUpdateApiView, BookDeleteApiView, \
    BookCreateApiView, BooksListCreateApiView, BooksUpdateDeleteApiView, BookViewSet
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register('books', BookViewSet, basename='books')

urlpatterns = [
    # path('books/v2/', books_list_view), #view's urls
    # path('books/', BooksListApiView.as_view()), #list
    # path('bookslistcreate/', BooksListCreateApiView.as_view()), #listcreate
    # path('bookupdatedelete/<int:pk>/', BooksUpdateDeleteApiView.as_view()), #updatedelete
    # path('books/create/', BookCreateApiView.as_view()), #create
    # path('books/<int:pk>/update/', BookUpdateApiView.as_view()), #update
    # path('books/<int:pk>/delete/', BookDeleteApiView.as_view()), #delete
    # path('book/<int:pk>/', BookDetailApiView.as_view()), #datails
]

urlpatterns += router.urls
