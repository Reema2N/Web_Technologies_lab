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

        # Lab 8
    path('lab8/task1', views.lab8_task1, name='lab8_task1'),
    path('lab8/task2', views.lab8_task2, name='lab8_task2'),
    path('lab8/task3', views.lab8_task3, name='lab8_task3'),
    path('lab8/task4', views.lab8_task4, name='lab8_task4'),
    path('lab8/task5', views.lab8_task5, name='lab8_task5'),
    path('lab8/task7', views.lab8_task7, name='lab8_task7'),
# Lab 9
    path('books/lab9/task1', views.lab9_task1),
    path('books/lab9/task2', views.lab9_task2),
    path('books/lab9/task3', views.lab9_task3),
    path('books/lab9/task4', views.lab9_task4),
    path('books/lab9/task5', views.lab9_task5),
    path('books/lab9/task6', views.lab9_task6),

# Lab 10
    path('lab9_part1/listbooks', views.list_books, name='list_books'),
    path('lab9_part1/addbook', views.add_book, name='add_book'),
    path('lab9_part1/editbook/<int:id>', views.edit_book, name='edit_book'),
    path('lab9_part1/deletebook/<int:id>', views.delete_book, name='delete_book'),

    path('lab9_part2/listbooks', views.list_books2, name='list_books2'),

    path('lab9_part2/addbook', views.add_book2, name='add_book2'),

    path('lab9_part2/editbook/<int:id>', views.edit_book2, name='edit_book2'),

    path('lab9_part2/deletebook/<int:id>', views.delete_book2, name='delete_book2'),
    ]

