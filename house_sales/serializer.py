from house_sales.models import SellHouses, SellVilla, SellGroundPlus, SellBuildings, SellAppartment, SellCondominum, SellStudio
from rest_framework import serializers

class SellHousesSerializer(serializers.ModelSerializer):
    time_since_upload = serializers.ReadOnlyField()
    
    class Meta:
        model = SellHouses
        fields = "__all__"

class SellVillaSerializer(serializers.ModelSerializer):
    time_since_upload = serializers.ReadOnlyField()
    
    class Meta:
        model = SellVilla
        fields = "__all__"

class SellGroundPlusSerializer(serializers.ModelSerializer):
    time_since_upload = serializers.ReadOnlyField()
    
    class Meta:
        model = SellGroundPlus
        fields = "__all__"

class SellBuildingsSerializer(serializers.ModelSerializer):
    time_since_upload = serializers.ReadOnlyField()
    
    class Meta:
        model = SellGroundPlus
        fields = "__all__"

class SellAppartmentSerializer(serializers.ModelSerializer):
    time_since_upload = serializers.ReadOnlyField()
    
    class Meta:
        model = SellAppartment
        fields = "__all__"

class SellCondominumSerializer(serializers.ModelSerializer):
    time_since_upload = serializers.ReadOnlyField()
    
    class Meta:
        model = SellCondominum
        fields = "__all__"

class SellStudioSerializer(serializers.ModelSerializer):
    time_since_upload = serializers.ReadOnlyField()
    
    class Meta:
        model = SellStudio
        fields = "__all__"