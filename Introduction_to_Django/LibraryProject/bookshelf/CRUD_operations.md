from bookshelf.models import Book
new_book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
new_book.save()


/**new_book.id 2**/

/**new_book.title '1984'**/

/**new_book.publication_year 1949**/

/**Book.objects.all() <QuerySet [<Book: 1984 by George Orwell, 1994>]>**/


/**retrieving**/

from bookshelf.models import Book 

Book.objects.all() <QuerySet [<Book: 1984 by George Orwell, 1994>]>


/**Updating**/

new_book.title = "Nineteen Eighty-Four" 

new_book.save()

/**new_book.title 'Nineteen Eighty-Four'**/


/**Delleting**/

new_book.delete() (1, {'bookshelf.Book': 2})

Book.objects.all()
<QuerySet []>