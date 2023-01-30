from rest_framework import generics
from .serializers import LojasTransacaoSerializers

from .models import TransacaoLojas

from rest_framework.views import status
from rest_framework.response import Response

from utils.function import formatarArquivo 

# Create your views here.
class LojasTransacaoView(generics.ListCreateAPIView):
    queryset = TransacaoLojas.objects.all()
    serializer_class = LojasTransacaoSerializers

    def create(self, request, *args, **kwargs):
        try:
            LojasTransacaoData = formatarArquivo(request.data["canab_arquivo"])

            serializer = LojasTransacaoSerializers(data=LojasTransacaoData)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        except:
            return Response({"canab_arquivo": "This field is required."}, status.HTTP_400_BAD_REQUEST)
