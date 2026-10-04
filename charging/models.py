from django.db import models


class ChargingSession(models.Model):

    class Status(models.TextChoices):
        SCHEDULED = "SCHEDULED", "Scheduled"
        ACTIVE = "ACTIVE", "Active"
        COMPLETED = "COMPLETED", "Completed"
        CANCELLED = "CANCELLED", "Cancelled"

    booking = models.OneToOneField(
        "bookings.Booking",
        on_delete=models.CASCADE,
        related_name="charging_session"
    )

    start_time = models.DateTimeField(
        null=True,
        blank=True
    )

    end_time = models.DateTimeField(
        null=True,
        blank=True
    )

    energy_consumed = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0
    )

    charging_cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    battery_start = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0
    )

    battery_end = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.SCHEDULED
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"Charging Session - {self.booking.booking_id}"