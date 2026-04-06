from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('create/', views.create_card),
    path('delete/<int:card_id>/', views.delete_card),
    path('image-search/', views.image_search),

]

