from rest_framework import serializers
from bookmanager.models import Book,ReservedBook


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        # fields = ['title','description','author','department','available_quantity','max_days_available','book_cover']
        fields = '__all__'

class ReservedBookSerializer(serializers.ModelSerializer):
    student = serializers.SerializerMethodField('get_student_details')
    reserved_book = serializers.SerializerMethodField('get_reserved_book')
    title = serializers.SerializerMethodField('get_reserved_title')
    book_cover = serializers.SerializerMethodField('get_reserved_bookimgUrl')
    class Meta:
        model = ReservedBook
        # fields = ['reserved_book',title,book_cover,'issue_date','due_date','student','returned_date']
        fields = '__all__'

    def get_student_details(self,obj):
        return obj.student.email
    def get_reserved_book(self,obj):
        return obj.reserved_book.id
    def get_reserved_title(self,obj):
        return obj.reserved_book.title
    def get_reserved_bookimgUrl(self,obj):
        return obj.reserved_book.book_cover
