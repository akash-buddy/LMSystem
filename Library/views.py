from django.shortcuts import render

# Create your views here.
# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Member, Transaction
from django.http import HttpResponse
from django.utils import timezone
from datetime import timedelta
import requests

# CRUD for Book
from django.db.models import Q

def book_list(request):
    query = request.GET.get("q", "")
    if query:
        books = Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )
    else:
        books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books, 'query': query})


def book_create(request):
    if request.method == 'POST':
        Book.objects.create(
            book_id=request.POST['book_id'],
            title=request.POST['title'],
            author=request.POST['author'],
            isbn=request.POST['isbn'],
            publisher=request.POST['publisher'],
            stock=request.POST['stock']
        )
        return redirect('book_list')
    return render(request, 'books/book_form.html')

def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.book_id=request.POST['book_id']
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.isbn = request.POST['isbn']
        book.publisher = request.POST['publisher']
        book.stock = request.POST['stock']
        book.save()
        return redirect('book_list')
    return render(request, 'books/book_form.html', {'book': book})

def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('book_list')

# Member CRUD (similar to books)
def member_list(request):
    members = Member.objects.all()
    return render(request, 'members/member_list.html', {'members': members})

def member_create(request):
    if request.method == 'POST':
        Member.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone']
        )
        return redirect('member_list')
    return render(request, 'members/member_form.html')

def member_update(request, pk):
    member = get_object_or_404(Member, pk=pk)
    if request.method == 'POST':
        member.name = request.POST['name']
        member.email = request.POST['email']
        member.phone = request.POST['phone']
        member.save()
        return redirect('member_list')
    return render(request, 'members/member_form.html', {'member': member})

def member_delete(request, pk):
    member = get_object_or_404(Member, pk=pk)
    member.delete()
    return redirect('member_list')

# Book Issue
def issue_book(request):
    if request.method == 'POST':
        member = Member.objects.get(id=request.POST['member'])
        book = Book.objects.get(id=request.POST['book'])

        if member.debt > 500:
            return HttpResponse("Cannot issue book. Member has debt over ₹500.")

        if book.stock == 0:
            return HttpResponse("Book out of stock")

        Transaction.objects.create(book=book, member=member)
        book.stock -= 1
        book.save()
        return redirect('issue_book')

    issued = Transaction.objects.filter(returned=False).order_by('-issue_date')
    return render(request, 'transactions/issue_book.html', {
        'members': Member.objects.all(),
        'books': Book.objects.all(),
        'issued': issued
    })

# Book Return
def return_book(request, pk):
    tx = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        days = (timezone.now().date() - tx.issue_date).days
        rent = 10 * days
        tx.rent_fee = rent
        tx.returned = True
        tx.return_date = timezone.now().date()
        tx.member.debt += rent
        tx.member.save()
        tx.book.stock += 1
        tx.book.save()
        tx.save()
        return redirect('book_list')

    return render(request, 'transactions/return_book.html', {'tx': tx})

# API Book Import
def import_books(request):
    if request.method == 'POST':
        title = request.POST.get("title", "")
        authors = request.POST.get("authors", "")
        isbn = request.POST.get("isbn", "")
        publisher = request.POST.get("publisher", "")
        count = int(request.POST.get("count", 20))

        books_imported = 0
        page = 1

        while books_imported < count:
            params = {"page": page}

            if title:
                params["title"] = title
            if authors:
                params["authors"] = authors
            if isbn:
                params["isbn"] = isbn
            if publisher:
                params["publisher"] = publisher
            res = requests.get("https://frappe.io/api/method/frappe-library", params=params)
            
            if res.status_code != 200:
                break

            data = res.json().get("message", [])
            
            if not data:
                break

            for book in data:
                if books_imported >= count:
                    break
                Book.objects.update_or_create(
                    book_id=book['bookID'],
                    defaults={
                        'title': book['title'],
                        'author': book.get('authors', ''),
                        'isbn': book.get('isbn', ''),
                        'publisher': book.get('publisher', ''),
                        'stock': 1
                    }
                )
                books_imported += 1

            page += 1

        return redirect('book_list')
    return render(request, "books/import_books.html")
