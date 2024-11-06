"""
URL configuration for hulu_be_ejewo_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib import admin
from user_management.views import RegisterUser, LogoutUser, ProfileView, user_details
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter
from house_rental.views import RentHouseViewSet, VillaViewSet, GroundPlusViewSet, BuildingsViewSet, AppartmentViewSet, CondominumViewSet, StudioViewSet, get_renthouse_detail, create_rent_house, create_villa_house, create_groundplus_house, create_appartment_house, create_buildings_house, create_condominum_house, create_studio_house
from django.conf.urls.static import static, settings
from house_sales.views import SellHouseViewSet, SellVillaViewSet, SellGroundPlusViewSet, SellBuildingsViewSet, SellAppartmentViewSet, SellCondominumViewSet, SellStudioViewSet, get_sellhouse_detail
from hulu_be_ejewo_backend.views import SearchEngine, TelegramPostsView

router = DefaultRouter()
router.register(r'RentHouse', RentHouseViewSet)
router.register(r'Villa', VillaViewSet)
router.register(r'GroundPlus', GroundPlusViewSet)
router.register(r'Building', BuildingsViewSet)
router.register(r'Appartment', AppartmentViewSet)
router.register(r'Condominum', CondominumViewSet)
router.register(r'Studio', StudioViewSet)

#For Selling House Router Are Displayed Here Below And my first comment 
#i don't comment at all

router.register(r'SellHouse', SellHouseViewSet)
router.register(r'SellVilla', SellVillaViewSet)
router.register(r'SellGroundPlus', SellGroundPlusViewSet)
router.register(r'SellBuilding', SellBuildingsViewSet)
router.register(r'SellAppartment', SellAppartmentViewSet)
router.register(r'SellCondominum', SellCondominumViewSet)
router.register(r'SellStudio', SellStudioViewSet)

urlpatterns = [ 
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('search/', SearchEngine.as_view(), name='search_engine'),
    path('api/register/', RegisterUser.as_view(), name='register'),
    path('api/user/', user_details.as_view(), name='user_details'),
    path('api/profile_view/', ProfileView.as_view(), name='profile_view'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/logout/', LogoutUser.as_view(), name='logout'),
    path('RentHouse/<int:id>/', get_renthouse_detail, name='renthouse-detail'),
    path('SellGroundPlus/<int:id>/', get_sellhouse_detail, name='sellhouse-detail'),
    path('api/house', create_rent_house, name='create_rent_house'),
    path('api/villa', create_villa_house, name='create_villa_house'),
    path('api/groundplus', create_groundplus_house, name='create_groundplus_house'),
    path('api/appartment', create_appartment_house, name='create_appartment_house'),
    path('api/buildings', create_buildings_house, name='create_buildings_house'),
    path('api/condominum', create_condominum_house, name='create_condominum_house'),
    path('api/studio', create_studio_house, name='create_studio_house'),
    path('api/telegram-posts', TelegramPostsView.as_view(), name='get_telegram_posts'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)