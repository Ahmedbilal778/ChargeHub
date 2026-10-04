from django.urls import path

from . import views


urlpatterns = [

    # =====================================================
    # AUTHENTICATION
    # =====================================================

    path(
        "login/",
        views.login_view,
        name="login"
    ),

    path(
        "register/",
        views.register_view,
        name="register"
    ),

    path(
        "logout/",
        views.logout_view,
        name="logout"
    ),


    # =====================================================
    # PROFILE
    # =====================================================

    path(
        "profile/",
        views.profile,
        name="profile"
    ),

    path(
        "profile/edit/",
        views.edit_profile,
        name="edit_profile"
    ),


    # =====================================================
    # SETTINGS
    # =====================================================

    path(
        "settings/",
        views.settings,
        name="settings"
    ),

    path(
        "settings/password/",
        views.change_password,
        name="change_password"
    ),

]