from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.handle_login),
    path('logout/',views.handle_logout),
    path('signup/',views.signup),
]