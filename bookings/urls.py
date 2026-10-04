from django.urls import path
from . import views


urlpatterns = [

    # Book Charger
    path(
        "book/<int:charger_id>/",
        views.book_charger,
        name="book_charger"
    ),

    # Booking Success
    path(
        "success/<int:booking_id>/",
        views.booking_success,
        name="booking_success"
    ),

    # My Bookings
    path(
        "my-bookings/",
        views.my_bookings,
        name="my_bookings"
    ),

    # Cancel Booking
    path(
        "cancel/<int:booking_id>/",
        views.cancel_booking,
        name="cancel_booking"
    ),

    # Charging History
    path(
        "charging-history/",
        views.charging_history,
        name="charging_history"
    ),

]