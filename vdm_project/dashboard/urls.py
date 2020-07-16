from django.urls import path
from . import views

urlpatterns = [
	path('homepage', views.homepage, name='homepage'),

    path('report/booking_list', views.booking_list, name='booking_list'),
    path('report/booking_list_day', views.booking_list_day, name='booking_list_day'),
    path('booking_detail/<str:bookingId>', views.booking_detail, name='booking_detail'),

    path('chart/dashboard360', views.dashboard360, name='dashboard360'),
    path('api/get_CA_days', views.get_CA_days, name='get_CA_days'),
    path('api/get_Nb_Bookings', views.get_Nb_Bookings, name='get_Nb_Bookings'),
    path('api/get_Nb_Spectators', views.get_Nb_Spectators, name='get_Nb_Spectators'),

    path('chart/dashboard_rooms', views.dashboard_rooms, name='dashboard_rooms'),
    path('api/get_CA_Rooms_Days', views.get_CA_Rooms_Days, name='get_CA_Rooms_Days'),
    path('api/get_CA_Rooms', views.get_CA_Rooms, name='get_CA_Rooms'),
    path('api/get_Spect_Rooms', views.get_Spect_Rooms, name='get_Spect_Rooms'),

    path('chart/dashboard_themes', views.dashboard_themes, name='dashboard_themes'),
    path('api/get_CA_Themes_Days', views.get_CA_Themes_Days, name='get_CA_Themes_Days'),
    path('api/get_CA_Themes', views.get_CA_Themes, name='get_CA_Themes'),
    path('api/get_Spect_Themes', views.get_Spect_Themes, name='get_Spect_Themes'),
    path('api/get_Points_Themes', views.get_Points_Themes, name='get_Points_Themes'),

    path('chart/dashboard_client', views.dashboard_client, name='dashboard_client'),
    path('api/get_Cust_Split_Sex_Daily', views.get_Cust_Split_Sex_Daily, name='get_Cust_Split_Sex_Daily'),
    path('api/get_Cust_Split_Sex', views.get_Cust_Split_Sex, name='get_Cust_Split_Sex'),
    path('api/get_Cust_Split_VR_Daily', views.get_Cust_Split_VR_Daily, name='get_Cust_Split_VR_Daily'),
    path('api/get_Cust_Split_VR', views.get_Cust_Split_VR, name='get_Cust_Split_VR'),
    path('api/get_Cust_Bookings_Hours', views.get_Cust_Bookings_Hours, name='get_Cust_Bookings_Hours'),
    path('api/get_Cust_Game_Hours', views.get_Cust_Game_Hours, name='get_Cust_Game_Hours'),
    path('api/get_Cust_Split_Age', views.get_Cust_Split_Age, name='get_Cust_Split_Age'),

    path('api/get_Spect_Split_Sex_Daily', views.get_Spect_Split_Sex_Daily, name='get_Spect_Split_Sex_Daily'),
    path('api/get_Spect_Split_Sex', views.get_Spect_Split_Sex, name='get_Spect_Split_Sex'),
    path('api/get_Spect_Split_VR_Daily', views.get_Spect_Split_VR_Daily, name='get_Spect_Split_VR_Daily'),
    path('api/get_Spect_Split_VR', views.get_Spect_Split_VR, name='get_Spect_Split_VR'),
    path('api/get_Spect_Bookings_Hours', views.get_Spect_Bookings_Hours, name='get_Spect_Bookings_Hours'),
    path('api/get_Spect_Game_Hours', views.get_Spect_Game_Hours, name='get_Spect_Game_Hours'),
    path('api/get_Spect_Split_Age', views.get_Spect_Split_Age, name='get_Spect_Split_Age'),

    path('data/data_extrator', views.data_extrator, name='data_extrator'),
]
