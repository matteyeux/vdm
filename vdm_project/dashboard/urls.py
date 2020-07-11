from django.urls import path
from . import views

urlpatterns = [
	path('homepage', views.homepage, name='homepage'),

    path('report/booking_list', views.booking_list, name='booking_list'),

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
]
