from decimal import Decimal
import uuid

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from bookings.models import Booking
from stations.models import Charger
from vehicles.models import Vehicle
from user_notifications.models import Notification

from .models import Payment


# =========================================================
# PAYMENTS LIST
# =========================================================

@login_required
def payment_list(request):

    payments = (
        Payment.objects
        .filter(
            user=request.user
        )
        .select_related(
            "booking",
            "booking__station",
            "booking__charger",
            "booking__vehicle"
        )
        .order_by(
            "-created_at"
        )
    )

    return render(
        request,
        "payments/payment_list.html",
        {
            "payments": payments
        }
    )


# =========================================================
# MAKE PAYMENT
# =========================================================

@login_required
def payment(request):

    # -----------------------------------------------------
    # GET PENDING BOOKING FROM SESSION
    # -----------------------------------------------------

    pending_booking = request.session.get(
        "pending_booking"
    )

    if not pending_booking:

        return redirect(
            "find_stations"
        )

    # -----------------------------------------------------
    # GET CHARGER
    # -----------------------------------------------------

    charger = get_object_or_404(
        Charger.objects.select_related(
            "station"
        ),
        id=pending_booking["charger_id"]
    )

    # -----------------------------------------------------
    # GET VEHICLE
    # -----------------------------------------------------

    vehicle = get_object_or_404(
        Vehicle,
        id=pending_booking["vehicle_id"],
        owner=request.user
    )

    # -----------------------------------------------------
    # PAYMENT SUBMIT
    # -----------------------------------------------------

    if request.method == "POST":

        payment_method = request.POST.get(
            "payment_method"
        )

        # -------------------------------------------------
        # VALIDATE PAYMENT METHOD
        # -------------------------------------------------

        if not payment_method:

            return render(
                request,
                "payments/payment.html",
                {
                    "charger": charger,
                    "vehicle": vehicle,
                    "pending_booking": pending_booking,
                    "error": "Please select a payment method."
                }
            )

        # -------------------------------------------------
        # GET BOOKING VALUES
        # -------------------------------------------------

        estimated_energy = Decimal(
            pending_booking["estimated_energy"]
        )

        estimated_amount = Decimal(
            pending_booking["estimated_amount"]
        )

        # -------------------------------------------------
        # CREATE BOOKING
        # -------------------------------------------------

        booking = Booking.objects.create(

            user=request.user,

            vehicle=vehicle,

            station=charger.station,

            charger=charger,

            booking_date=pending_booking[
                "booking_date"
            ],

            start_time=pending_booking[
                "start_time"
            ],

            end_time=pending_booking[
                "end_time"
            ],

            estimated_energy=estimated_energy,

            estimated_amount=estimated_amount,

            status=Booking.Status.CONFIRMED,

            notes=pending_booking.get(
                "notes",
                ""
            ),
        )

        # -------------------------------------------------
        # CREATE PAYMENT
        # -------------------------------------------------

        payment = Payment.objects.create(

            user=request.user,

            booking=booking,

            transaction_id=(
                f"CHG-"
                f"{uuid.uuid4().hex[:12].upper()}"
            ),

            amount=booking.estimated_amount,

            payment_method=payment_method,

            status=Payment.Status.SUCCESS,

            paid_at=timezone.now(),
        )

        # -------------------------------------------------
        # CREATE BOOKING NOTIFICATION
        # -------------------------------------------------

        Notification.objects.create(

            user=request.user,

            title="Booking Confirmed",

            message=(
                f"Your charging booking at "
                f"{charger.station.name} has been confirmed "
                f"for {pending_booking['booking_date']} "
                f"from {pending_booking['start_time']} "
                f"to {pending_booking['end_time']}."
            ),

            notification_type=(
                Notification.NotificationType.BOOKING
            ),

            is_read=False,
        )

        # -------------------------------------------------
        # REMOVE PENDING BOOKING
        # -------------------------------------------------

        del request.session[
            "pending_booking"
        ]

        request.session.modified = True

        # -------------------------------------------------
        # PAYMENT SUCCESS
        # -------------------------------------------------

        return redirect(
            "payment_success",
            payment_id=payment.id
        )

    # -----------------------------------------------------
    # PAYMENT PAGE
    # -----------------------------------------------------

    return render(
        request,
        "payments/payment.html",
        {
            "charger": charger,
            "vehicle": vehicle,
            "pending_booking": pending_booking,
        }
    )


# =========================================================
# PAYMENT SUCCESS
# =========================================================

@login_required
def payment_success(request, payment_id):

    payment = get_object_or_404(
        Payment.objects.select_related(
            "booking",
            "booking__station",
            "booking__charger",
            "booking__vehicle"
        ),
        id=payment_id,
        user=request.user
    )

    return render(
        request,
        "payments/payment_success.html",
        {
            "payment": payment
        }
    )