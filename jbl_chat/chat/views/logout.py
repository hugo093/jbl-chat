from braces.views import LoginRequiredMixin
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy


class LogoutMethodView(LoginRequiredMixin, LogoutView):
    success_url = reverse_lazy('login')
    http_method_names = ['post']