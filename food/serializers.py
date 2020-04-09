from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Food

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username','password','first_name','last_name']

    def create(self, validated_data):
        user = User(username=validated_data['username'],first_name = validated_data['first_name'],last_name = validated_data['last_name'] )
        user.set_password(validated_data['password'])
        user.save()
        return validated_data


class  FoodListSerializer(serializers.ModelSerializer):
    detail = serializers.HyperlinkedIdentityField(
        view_name = 'detail',
        lookup_field = 'id',
        lookup_url_kwarg = 'food_id'
    )
    class Meta:
        model = Food
        fields =['image', 'name','detail']


class FoodDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields =['image', 'name','description', 'price']

# class FoodCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Food
#         fields = ['name', 'description']

# class FoodUpdateSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Food
# 		fields = ['image', 'name','description']