# 📝 Django TODO App (AI Zoomcamp Lesson)

A simple Django TODO application created for AI Zoomcamp homework.  
This project demonstrates basic Django setup: project, app, models, views, templates, and running the server.

---

## 🚀 Setup

### 1. Create & activate virtual environment
```bash
python -m venv venv
source venv/bin/activate
2. Install Django
bash
Copy code
pip install django
3. Create project and app
bash
Copy code
django-admin startproject config .
python manage.py startapp todos
Add to config/settings.py:

python
Copy code
INSTALLED_APPS = [
    ...
    'todos',
]
🗃️ Model (todos/models.py)
python
Copy code
class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    due_date = models.DateField(null=True, blank=True)
    resolved = models.BooleanField(default=False)

    def __str__(self):
        return self.title
Run migrations:

bash
Copy code
python manage.py makemigrations
python manage.py migrate
🌐 Views (todos/views.py)
python
Copy code
def home(request):
    todos = Todo.objects.all().order_by("due_date")
    return render(request, "home.html", {"todos": todos})
🌍 URLs
todos/urls.py
python
Copy code
urlpatterns = [
    path("", views.home, name="home"),
]
config/urls.py
python
Copy code
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("todos.urls")),
]
🖼️ Templates
Set template directory in settings.py
python
Copy code
TEMPLATES[0]['DIRS'] = [BASE_DIR / "templates"]
templates/base.html
html
Copy code
<!DOCTYPE html>
<html>
<body>
<h1>TODO App</h1>
<hr>
{% block content %}{% endblock %}
</body>
</html>
templates/home.html
html
Copy code
{% extends "base.html" %}
{% block content %}
<h2>My TODOs</h2>
<ul>
    {% for todo in todos %}
        <li>{{ todo.title }} — {{ todo.due_date }} — {{ todo.resolved }}</li>
    {% empty %}
        <p>No TODOs yet.</p>
    {% endfor %}
</ul>
{% endblock %}
▶️ Run server
bash
Copy code
python manage.py runserver