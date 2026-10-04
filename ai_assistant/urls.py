from django.urls import path

from . import views


urlpatterns = [

    path(
        "charging-insights/",
        views.charging_insights,
        name="charging_insights"
    ),

]