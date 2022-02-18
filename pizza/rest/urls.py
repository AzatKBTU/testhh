from django.urls import path
from .views import ListRest, DetailRest, ListMenu, DetailMenu


urlpatterns = [
    path('rest/<int:pk>/', DetailRest.as_view()),
    path('rest/', ListRest.as_view()),
    path('menu/<int:pk>/', DetailMenu.as_view()),
    path('menu/', ListMenu.as_view()),
]