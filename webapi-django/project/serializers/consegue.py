from rest_framework import serializers
from project.models import consegue

class consegueSerializer(serializers.ModelSerializer):
	class Meta:
		model = consegue
		fields = '__all__'
