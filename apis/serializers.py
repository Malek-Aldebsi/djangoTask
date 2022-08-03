from rest_framework import serializers
from . import models
from .models import Order, Channel, Brand_branch, Fp_branch, Order_Item, Item, Order_item_add_ons, Add_ons, Fp, Brand


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ['name']


class fpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fp
        fields = ['name']

class Fp_branchSerializer(serializers.ModelSerializer):
    fp = fpSerializer(many=False)
    class Meta:
        model = Fp_branch
        fields = ['fp']


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['name']

class Brand_branchSerializer(serializers.ModelSerializer):
    Fp_branch = Fp_branchSerializer(many=False)
    brand = BrandSerializer(many=False)
    class Meta:
        model = Brand_branch
        fields = ['Fp_branch', 'brand']


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class Add_onsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Add_ons
        fields = '__all__'


class OrderItemAddOnesSerializer(serializers.ModelSerializer):
    # order_item = Order_ItemSerializer(many=False)
    Add_ons = Add_onsSerializer(many=False)
    class Meta:
        model = Order_item_add_ons
        fields = '__all__'


class Order_ItemSerializer(serializers.ModelSerializer):
    item = ItemSerializer(many=False)
    order_item_add_ons = OrderItemAddOnesSerializer(many=True)
    # order = OrderSerializer(many=False)
    class Meta:
        model = Order_Item
        fields = ['item', 'quantity', 'price', 'order_item_add_ons']


class OrderSerializer(serializers.ModelSerializer):
    channel = ChannelSerializer(many=False)
    brand_branch = Brand_branchSerializer(many=False)
    order_item = Order_ItemSerializer(many=True)
    class Meta:
        model = Order
        fields = ['id', 'channel', 'brand_branch', 'order_id', 'status', 'date_time', 'total', 'delivery_zone', 'customer_name', 'customer_mobile_number','payment_fees', 'delivary_fee', 'payment_method', 'order_item']

# class ItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Item
#         fields = '__all__'
