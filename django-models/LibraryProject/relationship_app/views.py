from django.shortcuts import render
from .models import Book
from .models import Library
from django.views.generic import TemplateView
from django.views.generic import DetailView
from django.views.generic.detail import DetailView
from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm

def book_list(request):
      """Retrieves all books and renders a template displaying the list."""
      books = Book.objects.all()  # Fetch all book instances from the database
      context = {'book_list': books}  # Create a context dictionary with book list
      return render(request, 'relationship_app/list_books.html', context)

# Create your views here.

class LibraryDetailView(DetailView):
  """A class-based view for displaying details of a specific book."""
  model = Library
  template_name = 'relationship_app/library_detail.html'

  def get_context_data(self, **kwargs):
    """Injects additional context data specific to the book."""
    context = super().get_context_data(**kwargs)  # Get default context data
    library = self.get_object()  # Retrieve the current library instance
    context['average_rating'] = library.get_average_rating() 



def login_view(request):
    return auth_views.LoginView.as_view(template_name="relationship_app/login.html")(
        request
    )


def logout_view(request):
    return auth_views.LogoutView.as_view(template_name="relationship_app/logout.html")(
        request
    )


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")  # Redirect to a home page after registration
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})
