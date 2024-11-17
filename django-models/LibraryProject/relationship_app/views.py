from django.shortcuts import render
from .models import Book
from .models import Library
from django.views.generic import TemplateView
from django.views.generic import DetailView

def book_list(request):
      """Retrieves all books and renders a template displaying the list."""
      books = Book.objects.all()  # Fetch all book instances from the database
      context = {'book_list': books}  # Create a context dictionary with book list
      return render(request, 'relationship_app/templates/list_books.html', context)

# Create your views here.

class LibraryDetailView(DetailView):
  """A class-based view for displaying details of a specific book."""
  model = Library
  template_name = 'relationship_app/templates/library_detail.html'

  def get_context_data(self, **kwargs):
    """Injects additional context data specific to the book."""
    context = super().get_context_data(**kwargs)  # Get default context data
    library = self.get_object()  # Retrieve the current library instance
    context['average_rating'] = library.get_average_rating() 


Implement Class-based View:

    Create a class-based view in relationship_app/views.py that displays details for a specific library,
     listing all books available in that library.
    Utilize Django’s ListView or DetailView to structure this class-based view.
