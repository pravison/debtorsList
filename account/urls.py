from django.urls import path, include
from . import views 

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('subscribe/', views.subscribe , name='subscribe'),
    path('launch_a_complain/', views.launchAcomplain , name='launch_a_complain'),
    path('send_a_message/', views.contactMessage , name='send_a_message'),
    path('terms/', views.terms , name='terms'),
    path('privacy/', views.privacy , name='privacy'),
]