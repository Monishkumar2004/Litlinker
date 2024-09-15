from django.urls import  path
from .views import *

app_name = 'apps'
urlpatterns =[

    path('', home, name = 'home'),
    path('book/<int:book_id>', details, name = 'details'),
    path('add/', add_book, name = 'add_book'),
    path('edit/<int:id>', edit_book, name = 'edit'),
    path('delete/<int:id>', delete_book, name = 'delete'),
    path('download/<int:id>', download_book, name = 'download'),
    # path('about/', about, name = 'about')


]