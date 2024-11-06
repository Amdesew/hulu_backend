#house models for rent and sells
from house_sales.models import SellAppartment, SellBuildings, SellCondominum, SellGroundPlus, SellHouses, SellStudio, SellVilla
from house_rental.models import RentHouses, Villa, GroundPlus, Appartment, Condominum, Studio

#house serializers for rent and sells
from house_sales.serializer import SellAppartmentSerializer, SellBuildingsSerializer, SellCondominumSerializer, SellGroundPlusSerializer, SellHousesSerializer, SellStudioSerializer, SellVillaSerializer
from house_rental.serializer import RentHousesSerializer, VillaSerializer, GroundPlusSerializer, AppartmentSerializer, CondominumSerializer, StudioSerializer

import requests
from bs4 import BeautifulSoup
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.db.models import Q
from django.http import JsonResponse


class SearchEngine(APIView):
    def get(self, request):
        query = request.GET.get('q', '')
        if query:
            houses = RentHouses.objects.filter(
                Q(details__icontains=query) |
                Q(location__icontains=query) |
                Q(description__icontains=query)
            )
            sell_houses = SellHouses.objects.filter(
                Q(details__icontains=query) |
                Q(location__icontains=query) |
                Q(description__icontains=query)
            )
            
            results = []
            results.extend([{
                "id": house.id,
                "details": house.details,
                "location": house.location,
                "image": house.image.url,
                "description": house.description
            } for house in houses])
            
            results.extend([{
                "id": sell_house.id,
                "details": sell_house.details,
                "location": sell_house.location,
                "image": sell_house.image.url,
                "description": sell_house.description
            } for sell_house in sell_houses])
            
        else:
            results = []
            
        return JsonResponse(results, safe=False)

class TelegramPostsView(APIView):
    def get(self, request):
        try:
            # Fetch the Telegram channel webpage
            url = 'https://t.me/s/Rental_house'
            response = requests.get(url)
            response.raise_for_status()
            
            # Parse the HTML content
            soup = BeautifulSoup(response.text, 'html.parser')
            posts = soup.find_all('div', class_='tgme_widget_message')
            
            # Extract data from each post
            formatted_posts = []
            for post in posts:
                # Find images - look for both photo and document classes
                photos = []
                photo_elements = post.find_all('a', class_='tgme_widget_message_photo_wrap')
                document_elements = post.find_all('a', class_='tgme_widget_message_document_wrap')
                
                # Extract photo URLs
                for photo in photo_elements:
                    if photo.get('style'):
                        # Extract URL from background-image style
                        style = photo.get('style', '')
                        if 'background-image:url(' in style:
                            url = style.split('url(\'')[1].split('\')')[0]
                            photos.append(url)
                    elif photo.find('img'):
                        # Extract URL from img src
                        img = photo.find('img')
                        if img and img.get('src'):
                            photos.append(img.get('src'))

                # Extract document URLs (for other media types)
                for doc in document_elements:
                    if doc.find('img'):
                        img = doc.find('img')
                        if img and img.get('src'):
                            photos.append(img.get('src'))

                # Create post data
                post_data = {
                    'id': post.get('data-post', ''),
                    'text': post.find('div', class_='tgme_widget_message_text').get_text() if post.find('div', class_='tgme_widget_message_text') else '',
                    'photos': photos,
                    'date': post.find('time', class_='time').get('datetime') if post.find('time', class_='time') else None
                }
                formatted_posts.append(post_data)

            # Return all posts after the loop is complete
            if not formatted_posts:
                return Response(
                    {'message': 'No posts found'}, 
                    status=status.HTTP_404_NOT_FOUND
                )
                
            # Return all formatted posts
            return Response(
                formatted_posts,
                status=status.HTTP_200_OK
            )
            
        except requests.RequestException as e:
            return Response(
                {'error': f'Failed to fetch Telegram posts: {str(e)}'}, 
                status=status.HTTP_503_SERVICE_UNAVAILABLE
            )
        except Exception as e:
            print(f"Error: {str(e)}")  # Add debug print
            return Response(
                {'error': f'An unexpected error occurred: {str(e)}'}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )