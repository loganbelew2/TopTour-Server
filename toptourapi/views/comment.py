from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from toptourapi.models import Comment, Tourist, Post

class CommentView(ViewSet):
    def list(self, request):
       comments = Comment.objects.all()
       if "post" in request.query_params:
            condition = request.query_params.get('post')
            filtered_comments = comments.filter(post__id = condition)
            serializer = CommentSerializer(filtered_comments, many=True)
       else:
            serializer = CommentSerializer(comments, many=True)
        
       return Response(serializer.data, status=status.HTTP_200_OK)
    def retrieve(self,__, pk):
        comment = Comment.objects.get(pk = pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self,__, pk):
        comment = Comment.objects.get(pk = pk)
        comment.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def create(self, request):
        comment = Comment.objects.create(
            content = request.data['content'],
            tourist = Tourist.objects.get(user = request.auth.user),
            post = Post.objects.get(pk = request.data['post'])
        )
        serializer = CommentSerializer(comment)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    def update(self, request, pk):
        comment = Comment.objects.get(pk=pk)
        serializer = CommentSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class CommentSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Comment
        fields = ('id', 'tourist', 'post', 'content', 'time_stamp')
        depth = 2