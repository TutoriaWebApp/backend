from rest_framework import serializers
from project.models import SessaoModel

class SessaoSerializer(serializers.ModelSerializer):
	class Meta:
		model  = SessaoModel
		fields = '__all__'
