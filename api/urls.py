from django.urls import path
from api import views

urlpatterns = [
    path('', views.BookListCreateView.as_view(), name='book-list'),
    path('<int:pk>/',views.BookDetail.as_view(), name='book-deatail'),
]
