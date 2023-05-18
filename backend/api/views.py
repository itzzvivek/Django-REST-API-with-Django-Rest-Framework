import json
from django.forms.models import model_to_dict  
# from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer


@api_view(["GET"])
def api_home(request, *args, **kwargs):
    """
    DRF API VIEW
    """
    # model_data = Product.objects.all().order_by("?").first()
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        # data = model_to_dict(instance, fields=['id','title','price','sale_price'])
        data = ProductSerializer(instance).data
        # data['id'] = model_data.id
        # data['title'] = model_data.title
        # data['content'] = model_data.content
        # data['price'] = model_data.price
        # serialization
        # model instance (model_data)
        # turn a python dict
        # return JSON to my client
    #return JsonResponse(data)
    return Response(data)
