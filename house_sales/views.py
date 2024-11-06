from django.shortcuts import render
from rest_framework.decorators import api_view
from house_sales.models import SellHouses, SellVilla, SellGroundPlus, SellBuildings, SellAppartment, SellCondominum, SellStudio
from house_sales.serializer import SellHousesSerializer, SellVillaSerializer, SellGroundPlusSerializer, SellBuildingsSerializer, SellAppartmentSerializer, SellCondominumSerializer, SellStudioSerializer
from rest_framework import viewsets, generics

class SellHouseViewSet(viewsets.ModelViewSet):
    queryset = SellHouses.objects.all()
    serializer_class = SellHousesSerializer

class SellVillaViewSet(viewsets.ModelViewSet):
    queryset = SellVilla.objects.all()
    serializer_class = SellVillaSerializer
    

class SellGroundPlusViewSet(viewsets.ModelViewSet):
    queryset = SellGroundPlus.objects.all()
    serializer_class = SellGroundPlusSerializer

class SellBuildingsViewSet(viewsets.ModelViewSet):
    queryset = SellBuildings.objects.all()
    serializer_class = SellBuildingsSerializer

class SellAppartmentViewSet(viewsets.ModelViewSet):
    queryset = SellAppartment.objects.all()
    serializer_class = SellAppartmentSerializer

class SellCondominumViewSet(viewsets.ModelViewSet):
    queryset = SellCondominum.objects.all()
    serializer_class = SellCondominumSerializer

class SellStudioViewSet(viewsets.ModelViewSet):
    queryset = SellStudio.objects.all()
    serializer_class = SellStudioSerializer

@api_view(['GET'])
def get_sellhouse_detail(request, id):
    try:
        print(f"Fetching house with ID: {id}")
        rent_house = SellHouses.objects.get(id=id)
        serializer = SellHousesSerializer(rent_house)
        return Response(serializer.data)
    except RentHouse.DoesNotExist:
        return Response({'error': 'House not found'}, status=404)