
from django.urls import path
from chat_rooms.views import newChat, selectRoom

urlpatterns = [
    path('newChat/', newChat),
    path('selectRoom/', selectRoom),
]
