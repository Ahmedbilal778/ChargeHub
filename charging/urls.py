from django.urls import path

from . import views


urlpatterns = [

    # Start Charging
    path(
        "start/<int:booking_id>/",
        views.start_charging,
        name="start_charging"
    ),

    # Complete Charging
    path(
        "complete/<int:booking_id>/",
        views.complete_charging,
        name="complete_charging"
    ),

]