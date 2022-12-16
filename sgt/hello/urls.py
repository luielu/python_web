from django.urls import path
from . import views

urlpatterns = [
	path("", views.index, name="index"),
	path("Luiza", views.Luiza, name="Luiza"),
	path("Lerigou", views.Lerigou, name="Lerigou"),
	path("<str:name>", views.greet, name="greet")
	
]
