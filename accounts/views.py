from django.contrib import messages
from django.contrib.auth import (
    authenticate,
    login,
    logout,
    update_session_auth_hash
)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect

from vehicles.models import Vehicle
from bookings.models import Booking

from .forms import RegisterForm


# =========================================================
# DASHBOARD
# =========================================================

@login_required
def dashboard(request):

    from stations.models import ChargingStation

    # -----------------------------------------------------
    # ACTIVE STATIONS WITH LOCATION
    # -----------------------------------------------------

    station_queryset = (
        ChargingStation.objects
        .filter(
            is_active=True,
            latitude__isnull=False,
            longitude__isnull=False
        )
        .prefetch_related("chargers")
    )

    # -----------------------------------------------------
    # PREPARE STATION DATA FOR MAP
    # QuerySet -> Python list/dictionary
    # -----------------------------------------------------

    stations = []

    for station in station_queryset:

        chargers = []

        for charger in station.chargers.all():

            chargers.append({
                "charger_type": charger.charger_type,
                "status": charger.status,
                "power_kw": float(charger.power_kw),
                "price_per_kwh": float(
                    charger.price_per_kwh
                ),
            })

        stations.append({

            "id": station.id,

            "name": station.name,

            "address": station.address,

            "city": station.city,

            "state": station.state,

            "latitude": float(
                station.latitude
            ),

            "longitude": float(
                station.longitude
            ),

            "chargers": chargers,

        })

    # -----------------------------------------------------
    # USER'S NEXT CONFIRMED BOOKING
    # -----------------------------------------------------

    next_booking = (
        Booking.objects
        .filter(
            user=request.user,
            status=Booking.Status.CONFIRMED
        )
        .select_related(
            "station",
            "charger",
            "vehicle"
        )
        .order_by(
            "booking_date",
            "start_time"
        )
        .first()
    )

    # -----------------------------------------------------
    # DASHBOARD
    # -----------------------------------------------------

    return render(
        request,
        "dashboard.html",
        {
            "stations": stations,
            "next_booking": next_booking,
        }
    )
# =========================================================
# PROFILE
# =========================================================

@login_required
def profile(request):

    vehicles_count = Vehicle.objects.filter(
        owner=request.user
    ).count()

    bookings_count = Booking.objects.filter(
        user=request.user
    ).count()

    charging_sessions = Booking.objects.filter(
        user=request.user,
        status=Booking.Status.COMPLETED
    ).count()

    return render(
        request,
        "accounts/profile.html",
        {
            "vehicles_count": vehicles_count,
            "bookings_count": bookings_count,
            "charging_sessions": charging_sessions,
        }
    )


# =========================================================
# EDIT PROFILE
# =========================================================

@login_required
def edit_profile(request):

    if request.method == "POST":

        first_name = request.POST.get(
            "first_name",
            ""
        ).strip()

        last_name = request.POST.get(
            "last_name",
            ""
        ).strip()

        email = request.POST.get(
            "email",
            ""
        ).strip()

        # ---------------------------------------------
        # UPDATE BASIC PROFILE INFORMATION
        # ---------------------------------------------

        request.user.first_name = first_name
        request.user.last_name = last_name
        request.user.email = email

        # ---------------------------------------------
        # UPDATE PROFILE IMAGE
        # ---------------------------------------------

        if request.FILES.get("profile_image"):

            request.user.profile_image = request.FILES[
                "profile_image"
            ]

        request.user.save()

        messages.success(
            request,
            "Profile updated successfully."
        )

        return redirect("profile")

    return render(
        request,
        "accounts/edit_profile.html"
    )


# =========================================================
# SETTINGS
# =========================================================

@login_required
def settings(request):

    return render(
        request,
        "accounts/settings.html"
    )


# =========================================================
# CHANGE PASSWORD
# =========================================================

@login_required
def change_password(request):

    if request.method == "POST":

        form = PasswordChangeForm(
            request.user,
            request.POST
        )

        if form.is_valid():

            user = form.save()

            # Keep user logged in after password change
            update_session_auth_hash(
                request,
                user
            )

            messages.success(
                request,
                "Password changed successfully."
            )

            return redirect("settings")

    else:

        form = PasswordChangeForm(
            request.user
        )

    return render(
        request,
        "accounts/change_password.html",
        {
            "form": form
        }
    )


# =========================================================
# LOGOUT
# =========================================================

@login_required
def logout_view(request):

    if request.method == "POST":

        logout(request)

        return redirect("login")

    return redirect("settings")


# =========================================================
# LOGIN
# =========================================================

def login_view(request):

    # Already logged in
    if request.user.is_authenticated:

        return redirect("dashboard")

    if request.method == "POST":

        username = request.POST.get(
            "username",
            ""
        ).strip()

        password = request.POST.get(
            "password",
            ""
        )

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(
                request,
                user
            )

            # If user was redirected to login
            # from a protected page, send them back there.
            next_url = request.POST.get(
                "next"
            )

            if next_url:
                return redirect(next_url)

            return redirect("dashboard")

        messages.error(
            request,
            "Invalid username or password."
        )

    return render(
        request,
        "accounts/login.html"
    )


# =========================================================
# REGISTER
# =========================================================

def register_view(request):

    # Already logged in
    if request.user.is_authenticated:

        return redirect("dashboard")

    if request.method == "POST":

        form = RegisterForm(
            request.POST
        )

        if form.is_valid():

            user = form.save()

            # Automatically login after registration
            login(
                request,
                user
            )

            messages.success(
                request,
                "Account created successfully."
            )

            return redirect("dashboard")

    else:

        form = RegisterForm()

    return render(
        request,
        "accounts/register.html",
        {
            "form": form
        }
    )