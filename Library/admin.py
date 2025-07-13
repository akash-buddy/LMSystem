

# Register your models here.

from django.contrib import admin
from .models import Book, Member, Transaction

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'book_id','title', 'author', 'isbn', 'stock')
    search_fields = ('title', 'author', 'isbn')

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'debt')
    search_fields = ('name', 'email', 'phone')

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'member', 'issue_date', 'return_date', 'rent_fee', 'returned')
    list_filter = ('returned', 'issue_date')
    search_fields = ('book__title', 'member__name')
