from django.urls import path
from . import views

urlpatterns = [
    path('Order/<str:pk>', views.getOrder),
    path('Channel/<str:pk>', views.getChannel),
    path('Status/<str:pk>', views.getStatus),
    path('DateTime/<str:pk>', views.getDate_time),
    path('Customer_name/<str:pk>', views.getCustomer_name),
    path('Customer_mobile_number/<str:pk>', views.getCustomer_mobile_number),
    path('Delivery_zone/<str:pk>', views.getDelivery_zone),
    path('ResturantName/<str:pk>', views.getResturantName),


    path('OrderItem/<str:pk>', views.getOrderItem),
    path('OrderAddOnes/<str:pk>', views.getOrderAddOnes),
]
