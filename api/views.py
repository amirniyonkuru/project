from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import (
    Product,
    Category,
    Order,
    OrderItem,
)
from .serializers import (
    ProductSerializer,
)


@api_view(["GET"])
def category(request, slug):
    if request.method == "GET":

        pk = [cat.id for cat in Category.objects.filter(slug=slug)]
        print(pk)
        prodct = Product.objects.raw(
            "SELECT * FROM api_product WHERE id NOT IN (select product_id from api_orderitem) AND category_id = %s",
            [pk],
        )

        if prodct:
            serializer = ProductSerializer(prodct, many=True)

            return Response(serializer.data)
        return Response("Not found")
