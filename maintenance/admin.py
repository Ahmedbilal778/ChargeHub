from django.contrib import admin
from .models import Maintenance


@admin.register(Maintenance)
class MaintenanceAdmin(admin.ModelAdmin):
    list_display = (
        "charger",
        "title",
        "priority",
        "status",
        "reported_at",
        "resolved_at",
    )

    list_filter = (
        "priority",
        "status",
    )

    search_fields = (
        "title",
        "description",
        "charger__charger_number",
    )