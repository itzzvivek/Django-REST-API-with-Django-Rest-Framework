from rest_framework import serializers

class UserProductinlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(view_name='product_detail',
                                               lookup_field='pk', read_only= 'True')
    title = serializers.CharField(read_only = True)

class UserPublicSerializer(serializers.Serializer):
    username = serializers.CharField(read_only = True)
    id = serializers.IntegerField(read_only=True)
    # other_products = serializers.SerializerMethodField(read_only = True)

    # def get_other_products(self,obj):
    #     user = obj
    #     my_products_qs = user.product_set.all()[:5]
    #     return UserProductinlineSerializer(my_product_qs, many=True, context=self.context).data