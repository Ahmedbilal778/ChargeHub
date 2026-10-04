from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from .models import ChargingStation


# =========================================================
# FIND STATIONS
# =========================================================

def find_stations(request):

    query = request.GET.get(
        "q",
        ""
    ).strip()


    stations = (
        ChargingStation.objects
        .filter(
            is_active=True
        )
        .prefetch_related(
            "chargers"
        )
    )


    # =====================================================
    # SEARCH
    # =====================================================

    if query:

        stations = stations.filter(

            Q(name__icontains=query)
            |
            Q(address__icontains=query)
            |
            Q(city__icontains=query)
            |
            Q(state__icontains=query)

        )


    return render(
        request,
        "stations/find_stations.html",
        {
            "stations": stations,
            "query": query,
        }
    )


# =========================================================
# STATION DETAIL
# =========================================================

def station_detail(
    request,
    station_id
):

    station = get_object_or_404(

        ChargingStation.objects
        .prefetch_related(
            "chargers"
        ),

        id=station_id,

        is_active=True

    )


    return render(
        request,
        "stations/station_detail.html",
        {
            "station": station
        }
    )