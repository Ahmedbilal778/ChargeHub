from datetime import datetime
from decimal import Decimal

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from stations.models import Charger
from vehicles.models import Vehicle

from .models import Booking


# =========================================================
# BOOK CHARGER
# =========================================================

@login_required
def book_charger(request, charger_id):

    charger = get_object_or_404(
        Charger.objects.select_related("station"),
        id=charger_id
    )

    vehicles = Vehicle.objects.filter(
        owner=request.user
    ).order_by(
        "-is_primary",
        "vehicle_name"
    )

    if request.method == "POST":

        vehicle_id = request.POST.get("vehicle")
        booking_date = request.POST.get("booking_date")
        start_time = request.POST.get("start_time")
        end_time = request.POST.get("end_time")
        notes = request.POST.get("notes", "")

        # -------------------------------------------------
        # GET USER VEHICLE
        # -------------------------------------------------

        vehicle = get_object_or_404(
            Vehicle,
            id=vehicle_id,
            owner=request.user
        )

        # -------------------------------------------------
        # VALIDATE TIME
        # -------------------------------------------------

        try:

            start = datetime.strptime(
                start_time,
                "%H:%M"
            )

            end = datetime.strptime(
                end_time,
                "%H:%M"
            )

        except (TypeError, ValueError):

            return render(
                request,
                "bookings/book_charger.html",
                {
                    "charger": charger,
                    "vehicles": vehicles,
                    "error": "Please enter a valid start and end time."
                }
            )

        # -------------------------------------------------
        # CALCULATE DURATION
        # -------------------------------------------------

        duration_seconds = (
            end - start
        ).total_seconds()

        duration_hours = Decimal(
            str(duration_seconds / 3600)
        )

        # -------------------------------------------------
        # CHECK INVALID TIME
        # -------------------------------------------------

        if duration_hours <= 0:

            return render(
                request,
                "bookings/book_charger.html",
                {
                    "charger": charger,
                    "vehicles": vehicles,
                    "error": "End time must be after start time."
                }
            )

        # -------------------------------------------------
        # CALCULATE ESTIMATED ENERGY
        #
        # Power (kW) × Duration (hours)
        # = Energy (kWh)
        # -------------------------------------------------

        estimated_energy = (
            Decimal(str(charger.power_kw))
            * duration_hours
        )

        # -------------------------------------------------
        # CALCULATE ESTIMATED AMOUNT
        #
        # Energy (kWh) × Price per kWh
        # = Amount
        # -------------------------------------------------

        estimated_amount = (
            estimated_energy
            * Decimal(str(charger.price_per_kwh))
        )

        # -------------------------------------------------
        # STORE PENDING BOOKING IN SESSION
        #
        # Booking is NOT created here.
        # It will be created after successful payment.
        # -------------------------------------------------

        request.session["pending_booking"] = {

            "charger_id": charger.id,

            "vehicle_id": vehicle.id,

            "booking_date": booking_date,

            "start_time": start_time,

            "end_time": end_time,

            "estimated_energy": str(
                estimated_energy
            ),

            "estimated_amount": str(
                estimated_amount
            ),

            "notes": notes,
        }

        # -------------------------------------------------
        # GO TO PAYMENT PAGE
        # -------------------------------------------------

        return redirect(
            "payment"
        )

    # -----------------------------------------------------
    # BOOKING PAGE
    # -----------------------------------------------------

    return render(
        request,
        "bookings/book_charger.html",
        {
            "charger": charger,
            "vehicles": vehicles,
        }
    )


# =========================================================
# BOOKING SUCCESS
# =========================================================

@login_required
def booking_success(request, booking_id):

    booking = get_object_or_404(
        Booking.objects.select_related(
            "charger",
            "station",
            "vehicle"
        ),
        id=booking_id,
        user=request.user
    )

    return render(
        request,
        "bookings/booking_success.html",
        {
            "booking": booking
        }
    )


# =========================================================
# MY BOOKINGS
# =========================================================

@login_required
def my_bookings(request):

    bookings = (
        Booking.objects
        .filter(
            user=request.user
        )
        .select_related(
            "station",
            "charger",
            "vehicle"
        )
        .order_by(
            "-booking_date",
            "-start_time"
        )
    )

    return render(
        request,
        "bookings/my_bookings.html",
        {
            "bookings": bookings
        }
    )


# =========================================================
# CANCEL BOOKING
# =========================================================

@login_required
def cancel_booking(request, booking_id):

    booking = get_object_or_404(
        Booking,
        id=booking_id,
        user=request.user
    )

    if request.method == "POST":

        booking.status = Booking.Status.CANCELLED

        booking.save()

    return redirect(
        "my_bookings"
    )


# =========================================================
# CHARGING HISTORY
# =========================================================

@login_required
def charging_history(request):

    history = (
        Booking.objects
        .filter(
            user=request.user,
            status__in=[
                Booking.Status.CONFIRMED,
                Booking.Status.COMPLETED,
            ]
        )
        .select_related(
            "vehicle",
            "station",
            "charger"
        )
        .order_by(
            "-booking_date",
            "-start_time"
        )
    )

    return render(
        request,
        "bookings/charging_history.html",
        {
            "history": history
        }
    )