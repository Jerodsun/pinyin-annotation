from rest_framework import serializers

from .models import UserInput

class UserInputSerializer(serializers.ModelSerializer):
    """ Serialize the user input string. """
    id = serializers.IntegerField(read_only=True)
    input_string = serializers.CharField(max_length=2000)

    class Meta:
        model = UserInput
        fields = ['id', 'created', 'input_string']

    def create(self, validated_data):
        return UserInput.objects.create(**validated_data)
