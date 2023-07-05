#from rest_framework.response import Response 
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
   # def post(self, request,*args,**kwargs):
   #     super().post(request,*args,**kwargs)
   #     return Response({}"message":"Book craeted"},status=200)


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
