from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

CATEGORY_CHOICES = (
    ('S', 'Shirt'),
    ('J', 'Jeans'),
    ('SW', 'Sport wear'),
    ('OW', 'Outwear')
)


class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    description = models.TextField()
    image = models.ImageField()

    def no_of_ratings(self):
        ratings = Rating.objects.filter(item=self)
        return len(ratings)
    
    @property
    def avg_rating(self):
        ratings = Rating.objects.filter(item=self)
        sum=0
        for rating in ratings:
            sum += rating.rating
        if len(ratings)>0:
            return sum/len(ratings)
        else:
            return None

    def __str__(self):
        return self.title

class Rating(models.Model):
    item = models.ForeignKey(Item, related_name='item', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    class Meta:
        unique_together = (('user', 'item'),)
        index_together = (('user', 'item'),)
