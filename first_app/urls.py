from django.urls import path
from . import views
urlpatterns=[
    path("register/", views.register, name="register"),
    path("signIn/", views.signIn, name="signIn"),
    path("profile/", views.profile, name="profile"),
    path("signOut/", views.signOut, name="singOut"),
    path("pass_change_with_old/", views.pass_change_with_old, name="pass_change_with_old"),
    path("pass_change_without_old/", views.pass_change_without_old, name="pass_change_without_old")
]