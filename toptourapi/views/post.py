from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from toptourapi.models import Post, Tourist, Attraction, Category

class PostView(ViewSet):
    def list(self, request):
        if 'user' in request.query_params:
            posts = Post.objects.filter(tourist_id = request.query_params['user'])
        else:
            posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self,__, pk):
        post = Post.objects.get(pk = pk)
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def update(self, request, pk):
        post = Post.objects.get(pk = pk)
        post.tourist = Tourist.objects.get(user = request.auth.user)
        post.attraction = Attraction.objects.get(pk = request.data['attraction'])
        post.category = Category.objects.get(pk = request.data['category'])
        post.review = request.data['review']
        post.name = request.data['name']
        post.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self,__, pk):
        post = Post.objects.get(pk = pk)
        post.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def create(self, request):
        post = Post.objects.create(
            tourist = Tourist.objects.get(user = request.auth.user),
            attraction = Attraction.objects.get(pk = request.data['attraction']),
            category = Category.objects.get(pk = request.data['category']),
            review = request.data['review'],
            name = request.data['name']
            )
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class PostSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Post
        fields = ('id', 'tourist', 'attraction', 'category', 'review', 'time_stamp', 'name')
        depth = 2