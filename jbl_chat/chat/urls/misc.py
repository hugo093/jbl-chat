from django.urls import path

from chat.views.home import HomeTemplateView
from chat.views.login import LoginFormView
from chat.views.logout import LogoutMethodView

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('auth/login', LoginFormView.as_view(), name='login'),
    path('auth/logout', LogoutMethodView.as_view(), name='logout')
]