from django.urls import path, include

from photo_gallery.accounts.views import UserSignIn, UserSignUp, UserSignOut, UserDetails, UserEdit, UserDelete, \
    UserGallery

urlpatterns = (
    path('register/', UserSignUp.as_view(), name='register'),
    path('login/', UserSignIn.as_view(), name='login'),
    path('logout/', UserSignOut.as_view(), name='logout'),
    path('profile/<int:pk>/', include([
        path('details/', UserDetails.as_view(), name='user profile'),
        path('edit/', UserEdit.as_view(), name='edit profile'),
        path('delete/', UserDelete.as_view(), name='delete profile'),
        path('gallery/', UserGallery.as_view(), name='profile gallery'),
    ]),
         ),

    )