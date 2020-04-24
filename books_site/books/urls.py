from django.urls import path
from . import views
app_name = 'books'
urlpatterns = [
    path('', views.home, name='name'),
    path('book/<int:book_id>/', views.detail, name='detail'),
]