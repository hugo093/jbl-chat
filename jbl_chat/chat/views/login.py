from django.contrib.auth.views import LoginView
from rest_framework.reverse import reverse_lazy


class LoginFormView(LoginView):
    template_name = "login.html"
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')
    redirect_field_name = "next"

    def get_redirect_url(self):
        redirect = super(LoginFormView, self).get_redirect_url()
        return reverse_lazy('home') if redirect == reverse_lazy('logout') else redirect