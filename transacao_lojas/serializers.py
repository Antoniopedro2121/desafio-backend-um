from rest_framework import serializers

from .models import TransacaoLojas

from lojas.models import Lojas

import ipdb

class LojasTransacaoSerializers(serializers.ModelSerializer):

    # canab_arquivo = serializers.FileField()

    class Meta:
        model = TransacaoLojas
        fields = '__all__'
        # depth = 1