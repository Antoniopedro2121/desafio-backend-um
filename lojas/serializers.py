from rest_framework import serializers

from .models import Lojas
from transacao_lojas.serializers import LojasTransacaoSerializers

class LojasSerializers(serializers.ModelSerializer):

    lojas_transacao = LojasTransacaoSerializers(many=True)

    class Meta:
        model = Lojas
        fields = '__all__'