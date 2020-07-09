from django.urls import path
from . import views

urlpatterns = [
    path('report/order', views.vdm_report_page, name='order_report'),
    path('report/booking_list', views.vdm_booking_list_page, name='booking_list'),
    path('chart/dashboard360', views.dashboard360, name='dashboard360'),
    path('api/get_CA_days', views.get_CA_days, name='get_CA_days'),
    path('api/get_CA_Rooms_Days', views.get_CA_Rooms_Days, name='get_CA_Rooms_Days'),
    path('api/get_CA_Rooms', views.get_CA_Rooms, name='get_CA_Rooms'),
    path('api/get_Spect_Rooms', views.get_Spect_Rooms, name='get_Spect_Rooms'),

    path('api/get_CA_Themes_Days', views.get_CA_Themes_Days, name='get_CA_Themes_Days'),
    path('api/get_CA_Themes', views.get_CA_Themes, name='get_CA_Themes'),
    path('api/get_Spect_Themes', views.get_Spect_Themes, name='get_Spect_Themes'),

    path('api/get_Points_Themes', views.get_Points_Themes, name='get_Points_Themes'),
]