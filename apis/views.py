from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import OrderSerializer
from .models import Order
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
def getOrderQuantity(request):
    id = request.data['id']
    Ord = Order.objects.get(id=id)
    serializer = OrderSerializer(Ord, many=False)
    return Response(serializer.data['order_Item']['quantity'])


@api_view(['POST'])
def getOrderItemName(request):
    id = request.data['id']
    Ord = Order.objects.get(id=id)
    serializer = OrderSerializer(Ord, many=False)
    return Response(serializer.data['order_Item']['item']['name'])

@api_view(['POST'])
def getOrderItemCost(request):
    id = request.data['id']
    Ord = Order.objects.get(id=id)
    serializer = OrderSerializer(Ord, many=False)
    return Response(serializer.data['order_Item']['item']['cost'])


@api_view(['POST'])
def getOrderAddOnesName(request):
    id = request.data['id']
    Ord = Order.objects.get(id=id)
    serializer = OrderSerializer(Ord, many=False)
    return Response(serializer.data['order_Item']['order_item_add_ones']['Add_ons']['name'])


@api_view(['POST'])
def getOrderAddOnesCost(request):
    id = request.data['id']
    Ord = Order.objects.get(id=id)
    serializer = OrderSerializer(Ord, many=False)
    return Response(serializer.data['order_Item']['order_item_add_ones']['Add_ons']['cost'])


@api_view(['POST'])
def getOrderTotalPrice(request):
    id = request.data['id']
    Ord = Order.objects.get(id=id)
    serializer = OrderSerializer(Ord, many=False)
    return Response(serializer.data['order_Item']['price'])

