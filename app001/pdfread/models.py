from django.db import models
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer, LTImage, LTRect, LTLine
from django.contrib.auth.models import User


def extract_pdf_content(pdf_path):
    content = []
    
    for page_layout in extract_pages(pdf_path):
        page_content = []
        for element in page_layout:
            if isinstance(element, LTTextContainer):
                # Extract Text
                page_content.append({
                    'type': 'text',
                    'data': element.get_text().strip()
                })
            elif isinstance(element, LTImage):
                page_content.append({
                    'type':'image',
                    'data':element.stream.get_rawdata()
                })
            # elif isinstance(element, (LTRect, LTLine)):
            #     # Extractes Shape (Optional)
            #     page_content.append({
            #         'type':'shape',
            #         'data':element
            #     })
        content.append(page_content)
    return content
            

# Create your models here.
class Books(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    title = models.CharField(max_length=100)
    slug = models.SlugField(blank=True)
    description = models.TextField(blank=True)
    
    pdf = models.FileField(upload_to='uploads/pdf')
    
    reading = models.CharField(max_length=100, blank=True)
    
    extracted_content = models.JSONField(blank=True, null=True)
    
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.title
    
    def extract_and_save_content(self):
        if self.pdf:
            pdf_path = self.pdf.path
            print(f"PDF pat: {pdf_path}")
            
            extracted_content = extract_pdf_content(pdf_path)
            
            self.extracted_content = extracted_content
            self.save()
        else:
            print("No pdf file Associated with this book")
    
class ReadingProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pdf_book = models.ForeignKey(Books, on_delete=models.CASCADE)
    last_page = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.pdf_book.title} - Page {self.last_page}"
    
    
class Category(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    
