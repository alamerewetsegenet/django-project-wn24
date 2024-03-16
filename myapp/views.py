from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.http import JsonResponse
from .default_data import load_default_data

from django.views.generic import ListView
from django.urls import reverse_lazy
from .models import Invention

from django.views.generic import DetailView



# Create your views here.
def home_view(request):
    context = {
      'page_title': 'Home-Based View',
      'page_heading': 'Welcome to the Home-Based View',
      'page_content': 'This is the content generated by the home-based view.',
    }
    return render(request, 'bootswatch.html', context)
    
def about_view(request):
    context = {
      'page_title': 'About-Based View',
      'page_heading': 'Welcome to the About-Based View',
      'page_content': 'This is the content generated by the about-based view.',
    }
    return render(request, 'bootswatch.html', context)

def surf_view(request):
    context = {
        'page_title': 'Surf-Based View',
        'page_heading': 'Welcome to the Surf-Based View',
        'page_content': 'This is the content generated by the surf-based view.',
    }
    return render(request, 'bootswatch.html', context)

def function_view(request):
    context = {
        'page_title': 'Function-Based View',
        'page_heading': 'Welcome to the Function-Based View',
        'page_content': 'This is the content generated by the function-based view.',
    }
    return render(request, 'bootswatch.html', context)

#class from which all class based views inherit
class BaseView(TemplateView):
    default_title = 'My Website'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.setdefault('title', self.default_title)
        return context

class ClassView(BaseView):
  template_name = 'bootswatch.html'

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context.update({
          'title': 'Class-Based View',
          'page_heading': 'Welcome to the Class-Based View',
          'page_content': 'This is the content generated by the class-based view.',
      })
      return context

class ThemeView(BaseView):
  template_name = 'theme.html'

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      # Add additional context data if needed
      return context

  def post(self, request, *args, **kwargs):
      theme = request.POST.get('theme')
      response = HttpResponseRedirect(reverse('theme'))
      response.set_cookie('theme', theme)
      return response


def load_default_data_view(request):
    load_default_data()  # Call the load_default_data function
    return JsonResponse({'status': 'success'})



class InventionListView(ListView):
    model = Invention
    template_name = 'invention_list.html'
    context_object_name = 'inventions'


class InventionDetailView(DetailView):
    model = Invention
    template_name = 'invention_view.html'
    context_object_name = 'invention'









