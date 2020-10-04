from account.models import Account
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Account
        fields = ['email','birth_date','status','date_joined','last_login','is_staff','is_admin']