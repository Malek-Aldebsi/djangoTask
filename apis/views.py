from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import OrderSerializer, Order_ItemSerializer, ItemSerializer, OrderItemAddOnesSerializer
from .models import Order, Order_Item


@api_view(['POST'])
def getOrder(request):
    id = request.data['id']
    Ord = Order.objects.get(id=id)
    serializer = OrderSerializer(Ord, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def getChannel(request):
    id = request.data['id']
    Ord = Order.objects.get(id=id)
    serializer = OrderSerializer(Ord, many=False)
    return Response(serializer.data['channel']['name'])


@api_view(['POST'])
def getStatus(request):
    id = request.data['id']
    Ord = Order.objects.get(id=id)
    serializer = OrderSerializer(Ord, many=False)
    return Response(serializer.data['status'])


@api_view(['POST'])
def getDate_time(request):
    id = request.data['id']
    Ord = Order.objects.get(id=id)
    serializer = OrderSerializer(Ord, many=False)
    return Response(serializer.data['date_time'])


@api_view(['POST'])
def getCustomer_name(request):
    id = request.data['id']
    Ord = Order.objects.get(id=id)
    serializer = OrderSerializer(Ord, many=False)
    return Response(serializer.data['customer_name'])


@api_view(['POST'])
def getCustomer_mobile_number(request):
    id = request.data['id']
    Ord = Order.objects.get(id=id)
    serializer = OrderSerializer(Ord, many=False)
    return Response(serializer.data['customer_mobile_number'])


@api_view(['POST'])
def getDelivery_zone(request):
    id = request.data['id']
    Ord = Order.objects.get(id=id)
    serializer = OrderSerializer(Ord, many=False)
    return Response(serializer.data['delivery_zone'])


@api_view(['POST'])
def getResturantName(request):
    id = request.data['id']
    Ord = Order.objects.get(id=id)
    serializer = OrderSerializer(Ord, many=False)
    return Response(serializer.data['brand_branch']['Fp_branch']['fp']['name'])


@api_view(['POST'])
def getOrderItem(request):
    id = request.data['id']
    Items = Order.objects.get(id=id).order_item_set.all()

    serializer = Order_ItemSerializer(Items, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def getOrderAddOnes(request):
    id = request.data['id']
    Add_ons = Order.objects.get(id=id).order_item_set.all()

    serializer = Order_ItemSerializer(Add_ons, many=True)
    return Response(serializer.data)
