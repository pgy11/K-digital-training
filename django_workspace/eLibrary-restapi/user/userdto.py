from rest_framework import serializers
from .models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # 내가 직렬화할 모델과, 필드를 Meta 클래스에 명시
        model = User
        fields = [
            'firstname', 
            'lastname', 
            'email', 
            'password', 
            'address', 
            'phonenumber'
            ]
  