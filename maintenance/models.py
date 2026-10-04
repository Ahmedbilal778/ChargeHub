from django.db import models


class Maintenance(models.Model):

    class Priority(models.TextChoices):
        LOW = "LOW", "Low"
        MEDIUM = "MEDIUM", "Medium"
        HIGH = "HIGH", "High"
        CRITICAL = "CRITICAL", "Critical"

    class Status(models.TextChoices):
        REPORTED = "REPORTED", "Reported"
        IN_PROGRESS = "IN_PROGRESS", "In Progress"
        COMPLETED = "COMPLETED", "Completed"
        CANCELLED = "CANCELLED", "Cancelled"

    charger = models.ForeignKey(
        "stations.Charger",
        on_delete=models.CASCADE,
        related_name="maintenance_records"
    )

    title = models.CharField(max_length=150)

    description = models.TextField()

    priority = models.CharField(
        max_length=20,
        choices=Priority.choices,
        default=Priority.MEDIUM
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.REPORTED
    )

    reported_at = models.DateTimeField(auto_now_add=True)

    resolved_at = models.DateTimeField(
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.charger} - {self.title}" 