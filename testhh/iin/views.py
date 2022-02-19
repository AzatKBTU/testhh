from rest_framework import generics
from .models import Person
from .serializers import PersonSerializer


class ListPerson(generics.ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class DetailPerson(generics.RetrieveAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

