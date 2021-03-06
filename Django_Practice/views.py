from django.urls import reverse_lazy
from django.views.generic.base import TemplateView

from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm


# --- Homepage View
class HomeView(TemplateView):
    template_name = 'home.html'


# --- User Creation
class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done') # 폼의 에러가 없을 시, 이동할 URL


class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'

