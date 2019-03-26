from rest_framework import serializers
from ecom.models import Users

class UserSerializer(serializers.ModelSerializer):
    class Meta:
            model = Users
            exclude = ['phone_number','created_date']