from rest_framework import serializers
from .models import (
    Product,
    Category,
    Order,
    OrderItem,
)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
