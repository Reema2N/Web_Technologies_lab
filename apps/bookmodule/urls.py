from django.urls import path
from . import views

#app_name = 'books'

urlpatterns = [
    path('', views.index, name="books.index"),
    path('list_books/', views.list_books, name="books.list_books"),
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    path('insert/', views.insert_book),
    path('books/simple/query', views.simple_query),
    path('books/complex/query', views.complex_query),

    # Lab 5
    path('html5/links', views.html5_links, name='html5_links'),
    path('html5/text/formatting', views.html5_text_formatting, name='html5_text_formatting'),
    path('html5/listing', views.html5_listing, name='html5_listing'),
    path('html5/tables', views.html5_tables, name='html5_tables'),

    # Lab 6
    path('search/', views.search_books, name='books.search'),
]