
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, get_user_model
from django.shortcuts import render

from photo_gallery.accounts.forms import UserCreateForm
from photo_gallery.photos.models import BasePhotos

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
        context['photos'] = BasePhotos.objects.all()
        return context


class UserEdit(views.UpdateView):
    template_name = 'accounts/edit-profile.html'
    model = UserModel
    fields = ('username', 'email', 'first_name', 'last_name', 'gender')

    def get_success_url(self):
        return reverse_lazy('user profile', kwargs={
            'pk': self.request.user.pk,
        })


class UserDelete(views.DeleteView):
    template_name = 'accounts/delete-profile.html'
    model = UserModel
    fields = '__all__'
    success_url = reverse_lazy('index')
