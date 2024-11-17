
from bookshelf.models import Book
new_book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
new_book.save()


/**new_book.id 2**/

/**new_book.title '1984'**/

/**new_book.publication_year 1949**/

/**Book.objects.all() <QuerySet [<Book: 1984 by George Orwell, 1994>]>**/