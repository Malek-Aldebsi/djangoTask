from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import OrderSerializer, Order_ItemSerializer, ItemSerializer, OrderItemAddOnesSerializer
from .models import Order, Order_Item, Order_item_add_ons


@api_view(['GET'])
def getOrder(request, pk):
    # id = request.data['id']
    Ord = Order.objects.get(id=pk)
    serializer = OrderSerializer(Ord, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def getChannel(request, pk):
    # id = request.data['id']
    Ord = Order.objects.get(id=pk)
    serializer = OrderSerializer(Ord, many=False)
    return Response(serializer.data['channel']['name'])


@api_view(['GET'])
def getStatus(request,pk):
    # id = request.data['id']
    Ord = Order.objects.get(id=pk)
    serializer = OrderSerializer(Ord, many=False)
    return Response(serializer.data['status'])


@api_view(['GET'])
def getDate_time(request, pk):
    # id = request.data['id']
    Ord = Order.objects.get(id=pk)
    serializer = OrderSerializer(Ord, many=False)
    return Response(serializer.data['date_time'])


@api_view(['GET'])
def getCustomer_name(request,pk):
    # id = request.data['id']
    Ord = Order.objects.get(id=pk)
    serializer = OrderSerializer(Ord, many=False)
    return Response(serializer.data['customer_name'])


@api_view(['GET'])
def getCustomer_mobile_number(request, pk):
    # id = request.data['id']
    Ord = Order.objects.get(id=pk)
    serializer = OrderSerializer(Ord, many=False)
    return Response(serializer.data['customer_mobile_number'])


@api_view(['GET'])
def getDelivery_zone(request,pk):
    # id = request.data['id']
    Ord = Order.objects.get(id=pk)
    serializer = OrderSerializer(Ord, many=False)
    return Response(serializer.data['delivery_zone'])


@api_view(['GET'])
def getResturantName(request,pk):
    # id = request.data['id']
    Ord = Order.objects.get(id=pk)
    serializer = OrderSerializer(Ord, many=False)
    return Response(serializer.data['brand_branch']['Fp_branch']['fp']['name'])


@api_view(['GET'])
def getOrderItem(request,pk):
    # id = request.data['id']
    Items = Order.objects.get(id=pk).order_item_set.all()

    serializer = Order_ItemSerializer(Items, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getOrderAddOnes(request, pk):
    # # id = request.data['id']
    # Add_ons = Order.objects.get(id=pk).order_item_set.all()
    #
    # serializer = Order_ItemSerializer(Add_ons, many=True)
    # return Response(serializer.data)
    i, j = 0, 0
    items = Order.objects.get(id=pk).order_item_set.all()
    itemNum = len(items)
    items = list(items)
    lst = []
    while i<itemNum:
        addOnesNum = len(items[i].order_item_add_ons_set.all())
        while j<addOnesNum:
            addOnes = items[i].order_item_add_ons_set.all()[j]
            lst.append(addOnes)
            j+=1
        j=0
        i+=1
    # Add_ons = Order_item_add_ons.objects.(order_item = order)

    serializer = OrderItemAddOnesSerializer(lst, many=True)
    return Response(serializer.data)

# @api_view(['GET'])
# def getOrderAddOnes(request, pk):
#     # # id = request.data['id']
#     # Add_ons = Order.objects.get(id=pk).order_item_set.all()
#     #
#     # serializer = Order_ItemSerializer(Add_ons, many=True)
#     # return Response(serializer.data)
#     i, j = 0, 0
#     items = Order.objects.get(id=pk).order_item_set.all()
#     itemNum = len(items)
#     items = list(items)
#     lst = []
#     while i<itemNum:
#         addOnesNum = len(items[i].order_item_add_ons_set.all())
#         while j<addOnesNum:
#             addOnes = items[i].order_item_add_ons_set.all()[j]
#             lst.append(addOnes)
#             j+=1
#         j=0
#         i+=1
#     # Add_ons = Order_item_add_ons.objects.(order_item = order)
#
#     serializer = OrderItemAddOnesSerializer(lst, many=True)
#     return Response(serializer.data)