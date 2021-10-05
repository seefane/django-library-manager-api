from django.urls import path
from . import views

urlpatterns = [path('books/',views.api_book_list,name='book-list'),
               path('reserve-book/<int:bookpk>/',views.api_reserve_book,name='book-reservation'),
               path('return-book/<int:bookpk>/',views.api_return_book,name='book-return'),
               path('confirm-return/<str:studendpk>/<int:bookpk>/',views.api_confrim_return,name='confirm-book-return'),
               path('user-reserved-books/', views.ApiUserReservedBooks.as_view(), name='user-reserved-books'),
               path('outstanding-books/', views.ApiOutstandingBooks.as_view())
               ]