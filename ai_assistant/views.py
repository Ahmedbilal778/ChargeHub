from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from vehicles.models import Vehicle
from bookings.models import Booking

from .gemini_service import generate_charging_insight


@login_required
def charging_insights(request):

    # =====================================================
    # USER'S PRIMARY VEHICLE
    # =====================================================

    vehicle = (
        Vehicle.objects
        .filter(
            owner=request.user,
            is_primary=True
        )
        .first()
    )

    # If no primary vehicle, get any vehicle
    if vehicle is None:

        vehicle = (
            Vehicle.objects
            .filter(
                owner=request.user
            )
            .first()
        )


    # =====================================================
    # BOOKING DATA
    # =====================================================

    total_bookings = Booking.objects.filter(
        user=request.user
    ).count()


    charging_sessions = Booking.objects.filter(
        user=request.user,
        status=Booking.Status.COMPLETED
    ).count()


    # =====================================================
    # PREPARE DATA FOR GEMINI
    # =====================================================

    user_data = {

        "vehicle": (
            vehicle.vehicle_name
            if vehicle
            else "No vehicle added"
        ),

        "battery_capacity": (
            vehicle.battery_capacity
            if vehicle
            else "Not available"
        ),

        "current_battery": (
            vehicle.current_battery
            if vehicle
            else "Not available"
        ),

        "total_bookings": total_bookings,

        "charging_sessions": charging_sessions,

        # Payment data will be connected later
        "average_cost": "Not available",
    }


    # =====================================================
    # GEMINI AI
    # =====================================================

    ai_insight = generate_charging_insight(
        user_data
    )


    # =====================================================
    # PAGE
    # =====================================================

    return render(
        request,
        "ai_assistant/charging_insights.html",
        {
            "ai_insight": ai_insight,

            "vehicle": vehicle,

            "total_bookings": total_bookings,

            "charging_sessions": charging_sessions,
        }
    )