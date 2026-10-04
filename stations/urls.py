from django.urls import path
from . import views


urlpatterns = [

    path(
        "",
        views.find_stations,
        name="find_stations"
    ),

    path(
        "<int:station_id>/",
        views.station_detail,
        name="station_detail"
    ),

]