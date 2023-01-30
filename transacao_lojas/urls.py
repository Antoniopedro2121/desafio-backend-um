from django.urls import path
from . import views

urlpatterns = [
    path("lojas/transacao/", views.LojasTransacaoView.as_view())
]