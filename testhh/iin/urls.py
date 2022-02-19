from django.urls import path
from .views import ListPerson, DetailPerson

urlpatterns = [
    path('<int:pk>/', DetailPerson.as_view()),
    path('', ListPerson.as_view()),
]
