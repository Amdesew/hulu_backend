from django.shortcuts import render
from rest_framework.decorators import api_view
from house_rental.models import RentHouses, Villa, GroundPlus, Buildings, Appartment, Condominum, Studio
from house_rental.serializer import RentHousesSerializer, VillaSerializer, GroundPlusSerializer, BuildingsSerializer, AppartmentSerializer, CondominumSerializer, StudioSerializer
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework import status

class RentHouseViewSet(viewsets.ModelViewSet):
    queryset = RentHouses.objects.all()
    serializer_class = RentHousesSerializer

class VillaViewSet(viewsets.ModelViewSet):
    queryset = Villa.objects.all()
    serializer_class = VillaSerializer
    

class GroundPlusViewSet(viewsets.ModelViewSet):
    queryset = GroundPlus.objects.all()
    serializer_class = GroundPlusSerializer

class BuildingsViewSet(viewsets.ModelViewSet):
    queryset = Buildings.objects.all()
    serializer_class = BuildingsSerializer

class AppartmentViewSet(viewsets.ModelViewSet):
    queryset = Appartment.objects.all()
    serializer_class = AppartmentSerializer

class CondominumViewSet(viewsets.ModelViewSet):
    queryset = Condominum.objects.all()
    serializer_class = CondominumSerializer

class StudioViewSet(viewsets.ModelViewSet):
    queryset = Studio.objects.all()
    serializer_class = StudioSerializer

@api_view(['GET'])
def get_renthouse_detail(request, id):
    try:
        print(f"Fetching house with ID: {id}")
        rent_house = RentHouses.objects.get(id=id)
        serializer = RentHousesSerializer(rent_house)
        return Response(serializer.data)
    except RentHouses.DoesNotExist:
        return Response({'error': 'House not found'}, status=404)

@api_view(['POST'])
def create_rent_house(request):
    if request.method == 'POST':
        serializer = RentHousesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_villa_house(request):
    if request.method == 'POST':
        serializer = VillaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_groundplus_house(request):
    if request.method == 'POST':
        serializer = GroundPlusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_buildings_house(request):
    if request.method == 'POST':
        serializer = BuildingsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_appartment_house(request):
    if request.method == 'POST':
        serializer = AppartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_condominum_house(request):
    if request.method == 'POST':
        serializer = CondominumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_studio_house(request):
    if request.method == 'POST':
        serializer = StudioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)