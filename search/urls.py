from django.urls import path
from .views import Index
app_name = 'search'

urlpatterns = [
    path('', Index, name='search_field')
]
