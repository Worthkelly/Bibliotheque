from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import *

class TokenPairSerializer(TokenObtainPairSerializer):
    	pass

class LivreSerializer(serializers.ModelSerializer):

	class Meta:
		model = Livre
		fields = "__all__"

class LecteurSerializer(serializers.ModelSerializer):
    
	class Meta:
		model = Lecteur
		fields = "__all_"

class RetraitSerializer(serializers.ModelSerializer):
    
	class Meta:
		model = Retrait
		fields = "__all_"

class RemiseSerializer(serializers.ModelSerializer):
	class Meta:
		model = Remise
		fields = "__all_"

		
