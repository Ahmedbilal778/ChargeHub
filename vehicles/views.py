from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .models import Vehicle


@login_required
def my_vehicles(request):

    vehicles = Vehicle.objects.filter(
        owner=request.user
    ).order_by(
        "-is_primary",
        "vehicle_name"
    )

    return render(
        request,
        "vehicles/my_vehicles.html",
        {
            "vehicles": vehicles
        }
    )


@login_required
def add_vehicle(request):

    if request.method == "POST":

        vehicle_name = request.POST.get("vehicle_name")
        vehicle_number = request.POST.get("vehicle_number")
        vehicle_type = request.POST.get("vehicle_type")
        battery_capacity = request.POST.get("battery_capacity")
        current_battery = request.POST.get("current_battery")
        range_km = request.POST.get("range_km")

        Vehicle.objects.create(
            owner=request.user,
            vehicle_name=vehicle_name,
            vehicle_number=vehicle_number,
            vehicle_type=vehicle_type,
            battery_capacity=battery_capacity,
            current_battery=current_battery,
            range_km=range_km,
        )

        return redirect("my_vehicles")

    return render(
        request,
        "vehicles/add_vehicle.html"
    )
@login_required
def edit_vehicle(request, vehicle_id):

    vehicle = get_object_or_404(
        Vehicle,
        id=vehicle_id,
        owner=request.user
    )

    if request.method == "POST":

        vehicle.vehicle_name = request.POST.get("vehicle_name")
        vehicle.vehicle_number = request.POST.get("vehicle_number")
        vehicle.vehicle_type = request.POST.get("vehicle_type")
        vehicle.battery_capacity = request.POST.get("battery_capacity")
        vehicle.current_battery = request.POST.get("current_battery")
        vehicle.range_km = request.POST.get("range_km")

        vehicle.save()

        return redirect("my_vehicles")

    return render(
        request,
        "vehicles/edit_vehicle.html",
        {
            "vehicle": vehicle
        }
    )
@login_required
def delete_vehicle(request, vehicle_id):

    vehicle = get_object_or_404(
        Vehicle,
        id=vehicle_id,
        owner=request.user
    )

    if request.method == "POST":
        vehicle.delete()

    return redirect("my_vehicles")