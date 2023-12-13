from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greetusers, name="greetusers"),
    path("statement", views.statement, name="statement"),
    path("routes", views.routes, name="routes")
]