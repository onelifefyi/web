from django.urls import path
from . import views             

urlpatterns = [
    path("", views.index, name="index"),
    path("vapor", views.vapor, name="vapor"),
    path("<str:name>", views.greet, name="greet")
]