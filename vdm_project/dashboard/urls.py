from django.urls import path
from . import views

urlpatterns = [
    path('report/order', views.vdm_report_page, name='order_report'),
    path('report/list_booking', views.vdm_list_booking_page, name='list_booking'),
]