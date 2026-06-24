from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('upload/', views.upload_document, name='upload_document'),
    path('document/<int:pk>/', views.document_detail, name='document_detail'),
    path('document/<int:pk>/delete/', views.delete_document, name='delete_document'),
    path('document/<int:pk>/edit/', views.edit_document, name='edit_document'),
    path('search/', views.search_documents, name='search_documents'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    # path('register/', views.register_view, name='register'),
]