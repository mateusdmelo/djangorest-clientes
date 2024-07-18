from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import cpf_valido, nome_valido
from clientes.validators import rg_valido, celular_valido


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({
                'cpf': "O CPF informado não é válido"
            })
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({
                'nome': "O nome deve conter apenas letras"
            })
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({
                'rg': "O RG deve ter 9 dígitos"
            })
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({
                'celular': "O celular deve seguir o modelo: (xx) xxxxx-xxxx"
            })
        return data
