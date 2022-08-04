from django.shortcuts import render
from django.http import HttpResponse

class Finch:  
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

finches = [
  Finch('Click', 'blue', 'Small and blue.', 3),
  Finch('Clack', 'saffron', 'Pretty and yellow.', 0),
  Finch('Thock', 'strawberry', 'Cute and red.', 4),
  Finch('Pop', 'gouldian', 'Bright and colorful.', 6)
]

# Create your views here.
def home(request):
  return HttpResponse('<h1>Hello</h1>')

def about(request):
  return render(request, 'about.html')

def finches_index(request):
  return render(request, 'finches/index.html', { 'finches': finches })