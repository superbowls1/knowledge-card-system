from django.urls import path
from . import views
# url patterns for card app
urlpatterns = [
#home page route and this shows all the display cards
    path('', views.home),
# this is showing   create a new card home
    path('create/', views.create_card),
# deleteing a specfifc card and its by its id
    path('delete/<int:card_id>/', views.delete_card),
    path('image-search/', views.image_search),
#image search page
]

