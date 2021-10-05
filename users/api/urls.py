from django.contrib.auth.decorators import login_required
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views


urlpatterns = [
    path('registration/',views.registration_view,name='registration'),
    path('login/',views.loginAuthtoken.as_view(),name='login'),
    path('update-details/<int:userpk>/',views.editUserinfo,name='editUserinfo'),

]