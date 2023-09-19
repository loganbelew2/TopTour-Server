from django.conf import settings
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status, serializers
import requests


class AttractionByIdView(ViewSet):

    def list(self, request):
        query = request.query_params.get('query')
        api_key = settings.GOOGLE_MAPS_API_KEY
        try:
            response = requests.get(
                f'https://maps.googleapis.com/maps/api/place/details/json?place_id={query}&key={api_key}'
            )

            if response.status_code == 200:
                data = response.json()
                attraction = data.get('result', {})
                serializer = AttractionDetailSerializer(attraction)
                return Response(serializer.data)

            return Response({'error': 'Failed to fetch data from Google Places API'}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class AttractionDetailSerializer(serializers.Serializer):
    name = serializers.CharField()
    address = serializers.CharField(source='formatted_address')
    coordinates = serializers.SerializerMethodField()
    icon_url = serializers.CharField(source='icon')
    rating = serializers.FloatField()
    total_ratings = serializers.IntegerField(source='user_ratings_total')
    photo_url = serializers.SerializerMethodField()

    def get_coordinates(self, obj):
        location = obj.get('geometry', {}).get('location', {})
        lat = location.get('lat', None)
        lng = location.get('lng', None)
        if lat is not None and lng is not None:
            return f'{lat}, {lng}'
        return None

    def get_photo_url(self, obj):
        photos = obj.get('photos', [])
        if photos:
            return photos[0].get('photo_reference')
        return None
