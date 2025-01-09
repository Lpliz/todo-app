from rest_framework.serializers import ModelSerializer
from .models import ToDoTask

class ToDoTaskSerializer(ModelSerializer):
    class Meta:
        model = ToDoTask
        fields = '__all__'