from apps.user.models import MentorUser
from rest_framework import serializers


class MentorUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MentorUser
        fields = '__all__'

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = self.Meta.model(**validated_data)
        user.set_password(password)
        user.save()
        return user