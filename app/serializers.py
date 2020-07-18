from rest_framework import serializers
from .models import Item, Rating

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields =('id', 'title', 'price', 'discount_price', 'description', 'category', 'image','no_of_ratings', 'avg_rating')


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('item', 'user', 'rating')