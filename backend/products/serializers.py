from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product
from .import validators
from api.serializer import UserPublicSerializer

class ProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='product_detail',
        lookup_field='pk', 
        read_only= 'True')
    title = serializers.CharField(read_only = True)


class ProductSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(source='user',read_only = True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='product_detail',
                                               lookup_field='pk')
    email = serializers.EmailField(write_only = True)
    title = serializers.CharField(validators=[validators.validate_title_no_hello,validators.unique_product_title])
    class Meta:
        model = Product
        fields = [
            'owner',
            'url',
            'edit_url',
            'pk',
            'title',
            'content',
            'price',
            'sale_price',
            'public',
        ]

    def get_my_user_data(self,obj):
        return{
            "username" :obj.user.username
        }

    def get_edit_url(self, obj):
        # return f"/api/products/{obj.pk}/"
        request = self.context.get('request') #self.request
        if request is None:
            return None
        return reverse("product-edit", kwargs={"pk": obj.pk} ,request=request)
        