from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone

from bookings.models import Booking
from .models import ChargingSession


@login_required
def start_charging(request, booking_id):

    booking = get_object_or_404(
        Booking,
        id=booking_id,
        user=request.user,
        status=Booking.Status.CONFIRMED
    )

    charging_session, created = ChargingSession.objects.get_or_create(
        booking=booking,
        defaults={
            "battery_start": booking.vehicle.current_battery,
            "status": ChargingSession.Status.SCHEDULED,
        }
    )

    charging_session.status = ChargingSession.Status.ACTIVE
    charging_session.start_time = timezone.now()
    charging_session.save()

    return redirect("my_bookings")


@login_required
def complete_charging(request, booking_id):

    booking = get_object_or_404(
        Booking,
        id=booking_id,
        user=request.user,
        status=Booking.Status.CONFIRMED
    )

    charging_session = get_object_or_404(
        ChargingSession,
        booking=booking
    )

    charging_session.status = ChargingSession.Status.COMPLETED
    charging_session.end_time = timezone.now()

    charging_session.save()

    booking.status = Booking.Status.COMPLETED
    booking.save()

    return redirect("charging_history")