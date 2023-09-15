from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from toptourapi.models import Tourist, Attraction, Category

class TouristView(ViewSet):
    def list(self,__):
        tourists = Tourist.objects.all()
        serializer = TouristSerializer(tourists, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self,__, pk):
        tourist = Tourist.objects.get(pk = pk)
        serializer = TouristSerializer(tourist)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def update(self, request, pk):
        tourist = Tourist.objects.get(pk = pk)
        tourist.bio = request.data['bio']
        tourist.profile_image = request.data['profile_image']
        tourist.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self,__, pk):
        tourist = Tourist.objects.get(pk = pk)
        tourist.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    

class TouristSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Tourist
        fields = ('id', 'user', 'bio', 'profile_image', 'full_name')
        depth = 1