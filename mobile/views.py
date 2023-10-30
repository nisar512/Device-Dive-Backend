from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Mobile

class MobileSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    brand = serializers.CharField()
    name = serializers.CharField()
    currency = serializers.CharField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    image = serializers.URLField(allow_null=True)

@api_view(['GET'])
def get_mobiles(request):
    mobiles = Mobile.objects.all()
    serializer = MobileSerializer(mobiles, many=True)
    return Response({'mobiles': serializer.data})



