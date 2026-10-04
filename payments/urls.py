from django.urls import path

from . import views


urlpatterns = [

    # =====================================================
    # PAYMENT HISTORY
    # =====================================================

    path(
        "",
        views.payment_list,
        name="payments"
    ),

    # =====================================================
    # MAKE PAYMENT
    # =====================================================

    path(
        "pay/",
        views.payment,
        name="payment"
    ),

    # =====================================================
    # PAYMENT SUCCESS
    # =====================================================

    path(
        "success/<int:payment_id>/",
        views.payment_success,
        name="payment_success"
    ),

]