from rest_framework import serializers
from project.models import Tutor

class TutorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tutor
		fields = '__all__'
