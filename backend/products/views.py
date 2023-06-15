from rest_framework import generics,mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from api.mixin import (
    StaffEditorPermissionMixin,
    UserQuerySetMixin)
#from django.http import Http404


from .models import Product
from .serializers import ProductSerializer

class ProductListCreateAPIView(
    UserQuerySetMixin,
    StaffEditorPermissionMixin,
    generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def perform_create(self,serializer):
        #serializer.save(user=self.request.user)
        # print(serializer.validated_data)
        email = serializer.validated_data.pop('email')
        # print(email)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(user=self.request.user,content=content)
        
        #send a django signals
    
    # def get_queryset(self, *args, **kwargs):
    #     qs = super().get_queryset(*args, **kwargs)
    #     request = self.request
    #     user =request.user
    #     if not user.is_authenticated:
    #         return Product.objects.none()
    #     print(request.user)
    #     return qs.filter(user=request.user)
    
product_list_create_view = ProductListCreateAPIView.as_view()


class ProductDetailAPIView(StaffEditorPermissionMixin,generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'

product_detail_view = ProductDetailAPIView.as_view()

class ProductUpdateAPIView(StaffEditorPermissionMixin,generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self,serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title 
            

product_update_view = ProductUpdateAPIView.as_view()

class ProductDestroyAPIView(UserQuerySetMixin,StaffEditorPermissionMixin,generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_destroy(self,instance):
        #instance
        super().perform_destroy(instance)
            

product_destroy_view = ProductDestroyAPIView.as_view()


# class ProductListAPIView(generics.RetrieveAPIView):
#     '''
#     not gonna use this method
#     '''
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     #lookup_field = 'pk'

# product_list_view = ProductListAPIView.as_view()

@api_view(['GET','POST'])
def product_alt_view(request,pk=None,*args,**kwargs):
    methods = request.method

    if method == 'GET':
        if pk is not None:
            #details view
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj,many=false).data
            return Response(data)
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data
        return Response(data)

    if method == "POST":
        #create an item
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)
        return Response({"invalid": "not good data"}, status=400)