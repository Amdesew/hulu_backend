from house_rental.models import RentHouses, Villa, GroundPlus, Buildings, Appartment, Condominum, Studio
from rest_framework import serializers

class RentHousesSerializer(serializers.ModelSerializer):
    time_since_upload = serializers.ReadOnlyField()
    
    class Meta:
        model = RentHouses
        fields = "__all__"

class VillaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Villa
        fields = "__all__"

class GroundPlusSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroundPlus
        fields = "__all__"

class BuildingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroundPlus
        fields = "__all__"

class AppartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appartment
        fields = "__all__"

class CondominumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Condominum
        fields = "__all__"

class StudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Studio
        fields = "__all__"