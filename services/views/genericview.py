from rest_framework import generics

from services.models import Employees
from services.serializers import employeesSerializer


class SnippetList(generics.ListCreateAPIView):
    queryset = Employees.objects.all()
    serializer_class = employeesSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employees.objects.all()
    serializer_class = employeesSerializer
