from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_document, name='upload_document'),
    path('document/<int:pk>/', views.document_detail, name='document_detail'),
    path('search/', views.search_documents, name='search_documents'),
]