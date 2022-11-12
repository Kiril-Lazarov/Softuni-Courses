from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, get_user_model
from django.shortcuts import render

from photo_gallery.accounts.forms import UserCreateForm

UserModel = get_user_model()


def get_profile(pk):
    try:
        return UserModel.objects.filter(pk=pk).get()
    except UserModel.DoesNotExist as ex:
        return None


class UserSignIn(auth_views.LoginView):
    template_name = 'accounts/login-page.html'
    success_url = reverse_lazy('index')


class UserSignOut(auth_views.LogoutView):
    next_page = reverse_lazy('index')


class UserSignUp(views.CreateView):
    template_name = 'accounts/register-page.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('user profile')


class UserDetails(views.DetailView):
    template_name = 'accounts/profile.html'
    model = UserModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['is_owner'] = self.request.user == self.object
        return context


