import uuid

from django.conf import settings
from django.db import models


class Booking(models.Model):

    class Status(models.TextChoices):
        PENDING = "PENDING", "Pending"
        CONFIRMED = "CONFIRMED", "Confirmed"
        COMPLETED = "COMPLETED", "Completed"
        CANCELLED = "CANCELLED", "Cancelled"

    booking_id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="bookings"
    )

    vehicle = models.ForeignKey(
        "vehicles.Vehicle",
        on_delete=models.CASCADE,
        related_name="bookings"
    )

    station = models.ForeignKey(
        "stations.ChargingStation",
        on_delete=models.CASCADE,
        related_name="bookings"
    )

    charger = models.ForeignKey(
        "stations.Charger",
        on_delete=models.CASCADE,
        related_name="bookings"
    )

    booking_date = models.DateField()

    start_time = models.TimeField()

    end_time = models.TimeField()

    estimated_energy = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        default=0
    )

    estimated_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING
    )

    notes = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"Booking {self.booking_id}"