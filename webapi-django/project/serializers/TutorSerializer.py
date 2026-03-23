from rest_framework import serializers
from project.models import TutorModel

class TutorSerializer(serializers.ModelSerializer):
	class Meta:
		model = TutorModel
		fields = '__all__'
