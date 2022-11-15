from . import forms
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, get_user_model, authenticate, login
from django.shortcuts import render, redirect
from django.views.generic import FormView

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
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        to_return = super().form_valid(form)
        user = authenticate(
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password1"],
        )
        login(self.request, user)
        return to_return




class UserDetails(views.DetailView):
    template_name = 'accounts/profile.html'
    model = UserModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['is_owner'] = self.request.user == self.object
        context['photos'] = BasePhotos.objects.filter(user_id=self.object.pk)
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


class UserGallery(views.DetailView):
    template_name = 'accounts/profile-gallery.html'
    model = UserModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['photos'] = BasePhotos.objects.filter(user_id=self.request.user.pk)
        return context
