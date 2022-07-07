
from django.urls import path
from users.views import KaKaoLoginView, kakao_callback

urlpatterns = [
    path('login/kakao', KaKaoLoginView.as_view()),
    path('kakao/login/callback/', kakao_callback)
]
