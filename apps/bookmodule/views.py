from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Q, Count, Sum, Avg, Max, Min
from .models import Book, Address, Student, Publisher, Author
from .forms import BookForm
def insert_book(request):
    Book.objects.create(
        title='Continuous Delivery',
        author='J.Humble and D. Farley',
        edition=1
    )

    return render(request, 'bookmodule/index.html')


def index(request):
    return render(request, "bookmodule/index.html")


def index2(request, val1=0):
    return HttpResponse("value1 = " + str(val1))


def list_books(request):
    return render(request, "bookmodule/list_books.html")


def viewbook(request, bookId):
    book1 = {'id': 123, 'title': 'Continuous Delivery', 'author': 'J. Humble and D. Farley'}
    book2 = {'id': 456, 'title': 'Secrets of Reverse Engineering', 'author': 'E. Eilam'}

    targetBook = None
    if book1['id'] == bookId:
        targetBook = book1
    if book2['id'] == bookId:
        targetBook = book2

    context = {'book': targetBook}
    return render(request, 'bookmodule/one_book.html', context)


def aboutus(request):
    return render(request, "bookmodule/aboutus.html")


def html5_links(request):
    return render(request, 'bookmodule/html5/links.html')


def html5_text_formatting(request):
    return render(request, 'bookmodule/html5/text_formatting.html')


def html5_listing(request):
    return render(request, 'bookmodule/html5/listing.html')


def html5_tables(request):
    return render(request, 'bookmodule/html5/tables.html')

def simple_query(request):
    mybooks = Book.objects.filter(title__icontains='and')
    return render(request, 'bookmodule/bookList.html', {'books': mybooks})

def complex_query(request):
    mybooks = Book.objects.filter(author__isnull=False)\
                          .filter(title__icontains='and')\
                          .filter(edition__gte=2)\
                          .exclude(price__lte=100)[:10]

    if len(mybooks) >= 1:
        return render(request, 'bookmodule/bookList.html', {'books': mybooks})
    else:
        return render(request, 'bookmodule/index.html')

def __getBooksList():
   book1 = {'id': 12344321, 'title': 'Continuous Delivery', 'author': 'J.Humble and D. Farley'}
   book2 = {'id': 56788765, 'title': 'Reversing: Secrets of Reverse Engineering', 'author': 'E. Eilam'}
   book3 = {'id': 43211234, 'title': 'The Hundred-Page Machine Learning Book', 'author': 'Andriy Burkov'}
   return [book1, book2, book3]

def search_books(request):
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')

        books = __getBooksList()
        newBooks = []

        for item in books:
            contained = False

            if isTitle and string in item['title'].lower():
                contained = True

            if not contained and isAuthor and string in item['author'].lower():
                contained = True

            if contained:
                newBooks.append(item)

        return render(request, 'bookmodule/bookList.html', {'books': newBooks})

    return render(request, 'bookmodule/search.html')


def lab8_task1(request):
    books = Book.objects.filter(Q(price__lte=80))
    return render(request, 'bookmodule/lab8/task1.html', {'books': books})

def lab8_task2(request):
    books = Book.objects.filter(
        Q(edition__gt=3) &
        (Q(title__icontains='qu') | Q(author__icontains='qu'))
    )
    return render(request, 'bookmodule/lab8/task2.html', {'books': books})

def lab8_task3(request):
    books = Book.objects.filter(
        ~Q(edition__gt=3) &
        ~(Q(title__icontains='qu') | Q(author__icontains='qu'))
    )
    return render(request, 'bookmodule/lab8/task3.html', {'books': books})

def lab8_task4(request):
    books = Book.objects.all().order_by('title')
    return render(request, 'bookmodule/lab8/task4.html', {'books': books})

def lab8_task5(request):
    total_books = Book.objects.count()

    stats = Book.objects.aggregate(
        total_price=Sum('price'),
        avg_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )

    context = {
        'total_books': total_books,
        'total_price': stats['total_price'],
        'avg_price': stats['avg_price'],
        'max_price': stats['max_price'],
        'min_price': stats['min_price'],
    }

    return render(request, 'bookmodule/lab8/task5.html', context)

def lab8_task7(request):
    cities = Address.objects.annotate(student_count=Count('student'))
    return render(request, 'bookmodule/lab8/task7.html', {'cities': cities})

def lab9_task1(request):
    books = Book.objects.all()

    total_quantity = 0
    for b in books:
        total_quantity += b.quantity

    for book in books:
        if total_quantity > 0:
            book.availability_percentage = (book.quantity / total_quantity) * 100
        else:
            book.availability_percentage = 0

    return render(request, 'bookmodule/lab9/task1.html', {'books': books})

def lab9_task2(request):
    publishers = Publisher.objects.annotate(total_books=Count('book'))

    return render(request, 'bookmodule/lab9/task2.html', {'publishers': publishers})

def lab9_task3(request):
    publishers = Publisher.objects.annotate(oldest_pubdate=Min('book__pubdate'))
    return render(request, 'bookmodule/lab9/task3.html', {'publishers': publishers})


def lab9_task4(request):
    publishers = Publisher.objects.annotate(
        avg_price=Avg('book__price'),
        min_price=Min('book__price'),
        max_price=Max('book__price')
    )

    return render(request, 'bookmodule/lab9/task4.html', {'publishers': publishers})

def lab9_task5(request):
    highly_rated = Count('book', filter=Q(book__rating__gte=7))

    publishers = Publisher.objects.annotate(
        highly_rated_books=highly_rated
    )

    return render(request, 'bookmodule/lab9/task5.html', {'publishers': publishers})

def lab9_task6(request):
    publishers = Publisher.objects.annotate(
        book_count=Count(
            'book',
            filter=Q(book__price__gt=50) & Q(book__quantity__lt=5) & Q(book__quantity__gte=1)
        )
    )

    return render(request, 'bookmodule/lab9/task6.html', {'publishers': publishers})

def list_books(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/list_books.html', {'books': books})


def add_book(request):

    if request.method == 'POST':

        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')
        edition = request.POST.get('edition')

        book = Book(
            title=title,
            author=author,
            price=price,
            edition=edition
        )

        book.save()

        return redirect('list_books')

    return render(request, 'bookmodule/add_book.html')


def edit_book(request, id):

    book = Book.objects.get(id=id)

    if request.method == 'POST':

        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.price = request.POST.get('price')
        book.edition = request.POST.get('edition')

        book.save()

        return redirect('list_books')

    return render(request, 'bookmodule/edit_book.html', {'book': book})


def delete_book(request, id):

    book = Book.objects.get(id=id)

    book.delete()

    return redirect('list_books')

def list_books2(request):

    books = Book.objects.all()

    return render(request,
                  'bookmodule/list_books2.html',
                  {'books': books})

def add_book2(request):

    if request.method == 'POST':

        form = BookForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('list_books2')

    else:
        form = BookForm()

    return render(request, 'bookmodule/add_book2.html', {'form': form})


def edit_book2(request, id):

    book = Book.objects.get(id=id)

    if request.method == 'POST':

        form = BookForm(request.POST, instance=book)

        if form.is_valid():
            form.save()

            return redirect('list_books2')

    else:

        form = BookForm(instance=book)

    return render(request,
                  'bookmodule/edit_book2.html',
                  {'form': form})


def delete_book2(request, id):

    book = Book.objects.get(id=id)

    book.delete()

    return redirect('list_books2')