from django.db import models
from .attraction import Attraction
from .tourist import Tourist
from .category import Category
class Post(models.Model):
    tourist = models.ForeignKey(Tourist, on_delete=models.CASCADE)
    attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    review = models.TextField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"Post {self.id}"
