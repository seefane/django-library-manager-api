from django.contrib import admin

from .models import Book, ReservedBook

admin.site.register(Book)
admin.site.register(ReservedBook)
