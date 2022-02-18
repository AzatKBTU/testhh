from rest_framework import generics
from .models import Restaurant, Menu
from .serializers import RestaurantSerializer, MenuSerializer


class ListRest(generics.ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
class DetailRest(generics.RetrieveAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
class ListMenu(generics.ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
class DetailMenu(generics.RetrieveAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
