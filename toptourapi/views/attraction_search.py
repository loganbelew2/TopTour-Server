# views.py

from django.conf import settings
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status, serializers
import requests


class AttractionSearchView(ViewSet):
    def list(self, request):
        query = request.query_params.get('query')
        api_key = settings.GOOGLE_MAPS_API_KEY
        print(api_key)
        try:
            # Make a request to the Google Places API
            response = requests.get(
                f'https://maps.googleapis.com/maps/api/place/textsearch/json?query={query}&key={api_key}&type=tourist_attraction'
            )

            # Check if the request was successful
            if response.status_code == 200:
                data = response.json()
                attractions = data.get('results', [])

                # Serialize the data
                serializer = TouristAttractionSerializer(attractions, many=True)
                return Response(serializer.data)

            return Response({'error': 'Failed to fetch data from Google Places API'}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class TouristAttractionSerializer(serializers.Serializer):
     name = serializers.CharField()
     formatted_address = serializers.CharField()