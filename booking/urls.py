from django.urls import path
from . import views
from .views import EditDanceBooking, DeleteDanceBooking

urlpatterns = [
    path("", views.dance_bookings, name="dance_bookings"),  # Home page for dance bookings
    path("booking_edit/<int:pk>/", EditDanceBooking.as_view(), name="edit_dance_booking"),  # Edit booking URL
    path("delete_booking/<int:pk>/", DeleteDanceBooking.as_view(), name="delete_dance_booking"),  # Delete booking URL
]
