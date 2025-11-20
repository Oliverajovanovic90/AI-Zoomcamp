from django.shortcuts import render
from .models import Todo

def home(request):
    todos = Todo.objects.all().order_by("due_date")
    return render(request, "home.html", {"todos": todos})