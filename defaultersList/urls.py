from django.urls import path
from . import views 

urlpatterns = [
    path('', views.search, name='search'),
    path('add-defaulter/', views.addDefaulter, name='add-defaulter'),
    path('search-results/', views.searchResults, name='search-results'),
    path('clear_defaulter/', views.clearDefaulter, name='clear_defaulter'),
    
]
