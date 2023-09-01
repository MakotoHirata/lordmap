from rest_framework import serializers
from snsapp.models import Account


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('last_name','first_name','account_image')