from rest_framework.serializers import ModelSerializer

from core.models.veiculo import Veiculo

class VeiculoSerializer(ModelSerializer):
    class Meta:
        model = Veiculo
        fields = "__all__"