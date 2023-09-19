from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
import requests

class PhotoView(ViewSet):
    def list(self, request):
        photo_ref = request.query_params.get('query')
        api_key = settings.GOOGLE_MAPS_API_KEY
        try:
            response = requests.get(
                f'https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photo_reference={photo_ref}&key={api_key}'
            )

            if response.status_code == 200:
                # Instead of trying to parse JSON, return the image content as a response
                image_content = response.url
                return Response(image_content)  # You can adjust content_type as needed

            return Response({'error': 'Failed to fetch image from Google Maps API'}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
