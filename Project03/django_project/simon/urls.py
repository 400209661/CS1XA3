from django.urls import path
from . views import ScoreListView
from . import views

urlpatterns = [
    path('', ScoreListView.as_view(), name='simon-home'),
    path('about/', views.about, name='about-page'),
]
