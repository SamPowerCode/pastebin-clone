from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_paste, name='create_paste'),
    path('paste_list/', views.paste_list, name='paste_list'),
    path('paste_detail/<int:pk>/', views.paste_detail, name='paste_detail'),  # Add this line
    # Add other URL patterns as needed
]
