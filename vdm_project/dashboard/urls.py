from django.urls import path
from . import views

urlpatterns = [
    path('report/order', views.vdm_report_page, name='order_report'),
    path('report/booking_list', views.vdm_booking_list_page, name='booking_list'),
    path('get/booking_list', views.get_booking_list, name='get_booking_list'),
]