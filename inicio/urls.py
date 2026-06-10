from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.hola, name="inicio"),
    path('login/', views.login_view, name="login"),
]
