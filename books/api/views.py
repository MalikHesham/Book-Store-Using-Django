from rest_framework.response import Response
from rest_framework import status

from books.models import Book
from .serializers import BookSerializer

from rest_framework.decorators import api_view


@api_view(["GET"])
def index(request):
    books = Book.objects.all()
    ser = BookSerializer(instance=books, many=True)
    return Response(data=ser.data,status=status.HTTP_200_OK)