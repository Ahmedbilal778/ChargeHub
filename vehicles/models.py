from django.conf import settings
from django.db import models


class Vehicle(models.Model):

    class VehicleType(models.TextChoices):
        CAR = "CAR", "Car"
        BIKE = "BIKE", "Bike"
        SCOOTER = "SCOOTER", "Scooter"

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="vehicles"
    )

    vehicle_name = models.CharField(
        max_length=100
    )

    vehicle_number = models.CharField(
        max_length=20,
        unique=True
    )

    vehicle_type = models.CharField(
        max_length=20,
        choices=VehicleType.choices,
        default=VehicleType.CAR
    )

    battery_capacity = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )

    current_battery = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0
    )

    range_km = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        default=0
    )

    is_primary = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.vehicle_name} - {self.vehicle_number}"