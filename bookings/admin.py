from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = (
        "booking_id",
        "user",
        "vehicle",
        "station",
        "charger",
        "booking_date",
        "start_time",
        "end_time",
        "status",
        "estimated_amount",
    )

    list_filter = (
        "status",
        "booking_date",
        "station",
    )

    search_fields = (
        "booking_id",
        "user__username",
        "station__name",
        "charger__charger_number",
    )

    readonly_fields = (
        "booking_id",
        "created_at",
        "updated_at",
    )

    ordering = (
        "-created_at",
    )