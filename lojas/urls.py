from django.urls import path
from . import views

urlpatterns = [
    path("lojas/", views.LojasView.as_view()),
    path("lojas/<int:pk>/", views.LojasViewByIdView.as_view())
]