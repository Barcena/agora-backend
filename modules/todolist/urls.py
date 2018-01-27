from django.urls import path
from django.views.generic import TemplateView
from .views import ToDoListView,ToDoDetailView

app_name = 'todolist'
urlpatterns = [

    path(r'', TemplateView.as_view(template_name='todo/todolist.html'), name= "todo"),
    path(r'api/', ToDoListView.as_view()),
    path(r'api/<int:pk>/', ToDoDetailView.as_view())
    
]