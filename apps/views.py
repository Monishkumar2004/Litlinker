from django.shortcuts import render, redirect
from django.http import HttpResponse, FileResponse
from .models import Book
from .forms import BookForm


# Create your views here.
def home(request):
    book_list = Book.objects.all()
    context = {
        'book_list': book_list
    }
    # return HttpResponse(book_list)
    return render(request, 'apps/index.html',context)

def details(request, book_id):
    # return HttpResponse("This is a Book with id %s" %book_id)

    book_details = Book.objects.get(id = book_id)
    context = {
        'book_details': book_details
    }

    return render(request, 'apps/details.html', context)

def add_book(request):
    if request.method == 'POST':
        # id = request.POST.get('id',)
        name = request.POST.get('name',)
        desc = request.POST.get('desc',)
        price = request.POST.get('price',)
        book_image = request.FILES['book_image']
        book_pdf = request.FILES['book_pdf']
        book = Book(name = name, desc = desc, price = price, book_image = book_image, pdf = book_pdf)
        book.save()


    return render(request, 'apps/add_book.html')

# def edit_book(request):
#     if request.method == 'POST':
#         id = request.POST.get('id',)
#         name = request.POST.get('name',)
#         desc= request.POST.get('desc',)
#         price = request.POST.get('price',)
#         book_image = request.FILES['book_image']

#         edit_book = Book.objects.get(id = id)
#         edit_book.name = name
#         edit_book.desc = desc
#         edit_book.price = price
#         edit_book.book_image = book_image

#         edit_book.save()


#     return render(request, 'apps/edit.html')


def edit_book(request, id):
    book  = Book.objects.get(id = id)
    form = BookForm(request.POST or None, request.FILES, instance= book)
    if form.is_valid():
        form.save()
        return redirect('/')
    context = {
        'form': form,
        'book': book 
    }    
    return render(request, 'apps/edit.html', context)    

def delete_book(request, id):
    if request.method == 'POST':
        book = Book.objects.get(id = id)
        book.delete()
        return redirect('/')
    return render(request, 'apps/delete.html')

def download_book(request, id):
    book = Book.objects.get(id = id)
    response = FileResponse(book.pdf.open(), content_type = 'application/pdf')
    response['Content-Disposition'] = f'attachment; filename = "{book.pdf.name}"' #This line helps download pdf as an attachment and it helps in not opening the pdf directly
    return response

