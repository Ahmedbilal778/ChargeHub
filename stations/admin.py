from django.contrib import admin
from .models import ChargingStation, Charger


@admin.register(ChargingStation)
class ChargingStationAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "city",
        "state",
        "opening_time",
        "closing_time",
        "is_active",
    )

    list_filter = (
        "city",
        "state",
        "is_active",
    )

    search_fields = (
        "name",
        "address",
        "city",
        "state",
    )


@admin.register(Charger)
class ChargerAdmin(admin.ModelAdmin):

    list_display = (
        "station",
        "charger_number",
        "charger_type",
        "power_kw",
        "price_per_kwh",
        "status",
        "is_active",
    )

    list_filter = (
        "charger_type",
        "status",
        "is_active",
    )

    search_fields = (
        "charger_number",
        "station__name",
    )