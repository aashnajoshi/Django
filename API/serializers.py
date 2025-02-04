from rest_framework import serializers
from app.models import Form

class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = '__all__'