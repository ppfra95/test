from rest_framework_mongoengine import serializers
from core.models import Customer


class CustomerSerializer(serializers.DocumentSerializer):

    class Meta:
        model = Customer
        fields = ('id',
                  'name',
                  'last_Name',
                  'age',
                  'address',
                  'email',
                  'cell_Phone')