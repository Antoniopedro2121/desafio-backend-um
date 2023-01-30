from rest_framework import generics
from .models import Lojas
from .serializers import LojasSerializers

# Create your views here.
class LojasView(generics.ListAPIView):
    queryset = Lojas.objects.all()
    serializer_class = LojasSerializers

    authentication_classes = []
    permission_classes = []

class LojasViewByIdView(generics.RetrieveAPIView):
    queryset = Lojas.objects.all()
    serializer_class = LojasSerializers

    authentication_classes = []
    permission_classes = []