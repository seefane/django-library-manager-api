from django.db.models import Q
from django.http import HttpResponse
from rest_framework import status,filters
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.response import  Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.generics import ListAPIView
from .serializers import BookSerializer, ReservedBookSerializer
from django.contrib.auth.models import User
from ..models import ReservedBook,Book

def is_student(obj, req):
    try:
        if req.user == obj.student:
            return True
    except:
        return False

    return False

@api_view(['GET'])
def api_book_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def api_reserve_book(request,pk):
    user = request.user
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return HttpResponse(status=404)
    if book.available_quantity > 0:
        reservedBook = ReservedBook(reserved_book=book, student=user)
        user_reserved_books = ReservedBook.objects.filter(student=user).filter(reserved_book=book.id)
        if user_reserved_books.count()==0:
            serializer = ReservedBookSerializer(reservedBook,data=request.data)
            if serializer.is_valid():
                serializer.save()

                book.decrement()
                book.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'Response':'Book already reserved'}, status=status.HTTP_403_FORBIDDEN)
    return Response({'Response':'The book is not available at the moment'},status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def api_return_book(request,pk):
    user = request.user
    try:
        user_reserved_book = ReservedBook.objects.filter(student=user).filter(Q(status="outstanding") | Q(status='return pending')).filter(reserved_book=pk)
        book = Book.objects.get(pk=pk)

    except ReservedBook.DoesNotExist and Book.DoesNotExist:
        return HttpResponse(status=404)

    if user_reserved_book.count()>0:
        serializer = ReservedBookSerializer(user_reserved_book.first(), data=request.data)
        if is_student(user_reserved_book.first(),request):
            if serializer.is_valid():
                serializer.save()
                book.increment()
                book.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({'response': 'You are not allowed to return this book'},status=status.HTTP_401_UNAUTHORIZED)

@api_view(['PUT'])
@permission_classes([IsAuthenticated,IsAdminUser])
def api_confrim_return(request,pk,std):
    user = request.user
    try:
        student = User.objects.get(username=std)
        user_reserved_book = ReservedBook.objects.filter(student=student).filter(Q(status="outstanding") | Q(status='return pending')).filter(reserved_book=pk)
        book = Book.objects.get(pk=pk)

    except ReservedBook.DoesNotExist and Book.DoesNotExist and User.DoesNotExist:
        return  HttpResponse(status=404)

    if user_reserved_book.count()>0:
        serializer = ReservedBookSerializer(user_reserved_book.first(), data=request.data)
        if user.is_superuser:
            if serializer.is_valid():
                serializer.save()
                book.increment()
                book.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({'response': 'Unthorized account'},status=status.HTTP_401_UNAUTHORIZED)



class ApiUserReservedBooks(ListAPIView):

    authentication_classes = [TokenAuthentication,SessionAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class =  ReservedBookSerializer
    # pagination_class = PageNumberPagination
    filter_backends = [filters.OrderingFilter]
    filterset_fields = ['title', 'description', 'student']

    def get_queryset(self):
        return self.request.user.reservedbook_set.all().order_by('-issue_date')

class ApiOutstandingBooks(ListAPIView):

    authentication_classes = [TokenAuthentication,SessionAuthentication]
    permission_classes = [IsAuthenticated,IsAdminUser]
    serializer_class =  ReservedBookSerializer
    # pagination_class = PageNumberPagination
    filter_backends = [filters.OrderingFilter]
    filterset_fields = ['title', 'description', 'student']

    def get_queryset(self):
            return ReservedBook.objects.filter(Q(status="outstanding") | Q(status='return pending'))









