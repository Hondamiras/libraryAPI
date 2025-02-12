from books.models import Books
from django.contrib import admin

# admin.site.register(Books)
@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'author', 'isbn', 'price')
    search_fields = ('title', 'subtitle', 'author', 'isbn')
    list_filter = ('title', 'subtitle', 'author', 'isbn', 'price')
    ordering = ('title', 'subtitle', 'author', 'isbn', 'price')
    list_per_page = 10
    list_max_show_all = 100
    list_editable = ('price', 'author')
    list_display_links = ('title', 'subtitle', 'isbn')
