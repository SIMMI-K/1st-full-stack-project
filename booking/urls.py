from django.urls import path
from . import views
from .views import Edit_dance_Booking, Delete_dance_Booking
# Ensure the correct import

urlpatterns = [
    path('', views.booking_view, name='booking'),
    # Home page for dance bookings
    path("booking_edit/<int:pk>/",
         Edit_dance_Booking.as_view(), name="edit_dance_booking"),
    # Edit booking URL
    path("delete_booking/<int:pk>/",
         Delete_dance_Booking.as_view(), name="delete_dance_booking"),
    # Delete booking URL
]
