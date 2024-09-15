from django.db import models

# Create your models here.

class Book(models.Model):

    name = models.CharField(max_length= 50)
    desc = models.CharField(max_length=100)
    # id = models.CharField(primary_key=True, max_length=10)
    price = models.IntegerField(default=0)
    book_image = models.ImageField(default='default.jpg', upload_to='book_images/')
    pdf = models.FileField(upload_to='books/pdfs/', null = True, blank=True)

    def __str__(self):
        return f'{self.id} {self.name} {self.desc}'

    