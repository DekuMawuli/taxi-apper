from django.urls import path
from . import views

app_name = "transport"

urlpatterns = [
    path("", views.home, name="landing_page"),
    path("all-drivers/", views.all_drivers, name="all_drivers"),
    path("drivers/", views.select_driver, name="select_driver"),
    path("book-driver/<int:pk>/", views.book_driver, name="book_ride"),
    path("process-book-ride/<int:pk>/", views.booking_ride_process, name="process_booking"),
    path("accepting-booking/<int:pk>/", views.approve_ride, name="approve_ride"),
    path("about-us/", views.about, name="about_us"),
    path("contact-us/", views.contact, name="contact_us"),
    path("driver-login/", views.driver_login, name="login_driver"),
    path("update-profile/", views.update_profile, name="update_profile"),
    path("register-driver/", views.driver_register, name="register_driver"),
    path("process-register/", views.process_registration, name="process_driver_register"),
    path("process-login/", views.process_login, name="process_driver_login"),
    path("profile/", views.driver_profile, name="driver_profile"),
    path("dashboard/", views.driver_dashboard, name="driver_dashboard"),
    path("logout/", views.driver_logout, name="driver_logout"),

]