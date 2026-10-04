from django.db import models


# =========================================================
# CHARGING STATION
# =========================================================

class ChargingStation(models.Model):

    name = models.CharField(
        max_length=150
    )

    address = models.TextField()

    city = models.CharField(
        max_length=100
    )

    state = models.CharField(
        max_length=100
    )

    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True
    )

    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True
    )

    opening_time = models.TimeField()

    closing_time = models.TimeField()

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):

        return self.name


# =========================================================
# CHARGER
# =========================================================

class Charger(models.Model):

    class ChargerType(models.TextChoices):

        CCS2 = "CCS2", "CCS2"

        TYPE2 = "TYPE2", "Type 2"

        CHADEMO = "CHADEMO", "CHAdeMO"

        TESLA = "TESLA", "Tesla"


    class Status(models.TextChoices):

        AVAILABLE = "AVAILABLE", "Available"

        OCCUPIED = "OCCUPIED", "Occupied"

        MAINTENANCE = "MAINTENANCE", "Maintenance"

        OFFLINE = "OFFLINE", "Offline"


    station = models.ForeignKey(
        ChargingStation,
        on_delete=models.CASCADE,
        related_name="chargers"
    )

    charger_number = models.CharField(
        max_length=50
    )

    charger_type = models.CharField(
        max_length=20,
        choices=ChargerType.choices
    )

    power_kw = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )

    price_per_kwh = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.AVAILABLE
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):

        return (
            f"{self.station.name} - "
            f"{self.charger_number}"
        )