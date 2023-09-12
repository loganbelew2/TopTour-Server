from django.db import models
from .tourist import Tourist
from .post import Post
class Comment(models.Model):
    tourist = models.ForeignKey(Tourist, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment {self.id}"
