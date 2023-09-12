from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from toptourapi.models import Attraction

class AttractionView(ViewSet):
    def list(self,__):
        attractions = Attraction.objects.all()
        serializer = AttractionSerializer(attractions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self,__, pk):
        attraction = Attraction.objects.get(pk = pk)
        serializer = AttractionSerializer(attraction)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def update(self, request, pk):
        attraction = Attraction.objects.get(pk = pk)
        attraction.name = request.data['name']
        attraction.address = request.data['address']
        attraction.coordinates = request.data['coordinates']
        attraction.icon_url = request.data['icon_url']
        attraction.rating = request.data['rating']
        attraction.total_ratings = request.data['total_ratings']
        attraction.photo_url = request.data['photo_url']
        attraction.price_level = request.data['price_level']
        attraction.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self,__, pk):
        attraction = Attraction.objects.get(pk = pk)
        attraction.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def create(self, request):
        attraction = Attraction.objects.create(
            name = request.data['name'],
            address = request.data['address'],
            coordinates = request.data['coordinates'],
            icon_url = request.data['icon_url'],
            rating = request.data['rating'],
            total_ratings = request.data['total_ratings'],
            photo_url = request.data['photo_url'],
            price_level = request.data['price_level']
            )
        serializer = AttractionSerializer(attraction)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class AttractionSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Attraction
        fields = ('id', 'name', 'address', 'coordinates', 'icon_url', 'rating', 'total_ratings', 'photo_url', 'price_level')
        depth = 1