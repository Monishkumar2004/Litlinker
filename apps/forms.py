from django import forms    #Imports django's form module
from .models import Book    # Imports book from models.py

class BookForm(forms.ModelForm): #forms.ModelsForm generated auto Fields and does validations for input according to the models.py 
    class Meta:
        model = Book    # This tell Django that model is associated with Book model
        fields = ['name', 'desc', 'price', 'book_image']



