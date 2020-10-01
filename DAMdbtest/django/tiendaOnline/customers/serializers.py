from rest_framework_mongoengine import serializers
from core.models import Customer


class CustomerSerializer(serializers.DocumentSerializer):

    class Meta:
        model = Customer
        fields = '__all__'
        # fields = ('id',
        #           'name',
        #           'last_Name',
        #           'age',
        #           'address',
        #           'email',
        #           'password',
        #           'cell_Phone')
