from django.shortcuts import render, redirect, get_object_or_404
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer, LTImage, LTRect, LTLine
from .models import Books
from .forms import PDFform


# Create your views here.
def index(request):
    books = Books.objects.all()
    
    context = {
        "books":books
    }
    return render(request, "pdfread/index.html", context)


def read_book(request, pdf_id):
    pdf = get_object_or_404(Books, id=pdf_id)
    
    
    context = {
        "pdf":pdf
    }
    return render(request, "pdfread/read.html", context)

def upload_pdf(request):
    form = PDFform()
    if request.method == "POST":
        print(request.FILES)
        form = PDFform(request.POST, request.FILES)
        if form.is_valid():
            pdf_book = form.save(commit=False)
            
            pdf_book.user = request.user
            pdf_book.save()
            
            pdf_book.extract_and_save_content()
            
            return redirect('pdfread:index')
    else:
        form = PDFform()
        return render(request, 'pdfread/upload.html', {'form':form})
    return render(request, 'pdfread/upload.html', {'form':form})
            
