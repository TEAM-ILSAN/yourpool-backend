
from django.urls import path
from users.views import KaKaoLoginView, kakao_callback, updateroom, updategeo

urlpatterns = [
    path('login/kakao', KaKaoLoginView.as_view()),
    path('kakao/login/callback/', kakao_callback),
    path('updategeo/', updategeo),
]
