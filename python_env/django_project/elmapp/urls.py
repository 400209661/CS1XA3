from django.urls import path
from . import views

urlpatterns = [
	path('', views.elm_app , name='elmapp-elm'),
]
