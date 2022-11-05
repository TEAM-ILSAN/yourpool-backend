
from django.urls import path
from chat_rooms.views import newChat, selectRoom, intoRoom, chatList

urlpatterns = [
    path('newChat/', newChat),
    path('selectRoom/', selectRoom),
    path('intoRoom/', intoRoom),
    path('chatList/', chatList),
]
