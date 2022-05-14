
from django.urls import path
from users.views import KaKaoLoginView, KaKaoLoginCallBackView

urlpatterns = [
    path('login/kakao', KaKaoLoginView.as_view()),
    path('kakao/login/callback/', KaKaoLoginCallBackView.as_view())
]
