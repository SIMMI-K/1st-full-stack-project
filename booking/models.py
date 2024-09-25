from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
# Predefined time choices for booking 
BOOKING_TIME = (
    (datetime.time(9, 0, 0), "9:00am"),
    (datetime.time(10, 0, 0), "10:00am"),
    (datetime.time(11, 0, 0), "11:00am"),
    (datetime.time(12, 0, 0), "12:00pm"),
    (datetime.time(13, 0, 0), "1:00pm"),
    (datetime.time(14, 0, 0), "2:00pm"),
    (datetime.time(15, 0, 0), "3:00pm"),
    (datetime.time(16, 0, 0), "4:00pm"),
)

# Choices for different dance styles
DANCE_STYLES = (
    ("Ballet", "Ballet"),
    ("Hip Hop", "Hip Hop"),
    ("Salsa", "Salsa"),
    ("Indian classical", "Indian classical"),
)
class DanceClass(models.Model):
    """
    Model for displaying details of available dance classes.

    Fields:
        - `title` (CharField): Name of the dance class.
        - `description` (TextField): Description of the dance class.
        - `updated_on` (DateTimeField): Last update timestamp.
    """

    title = models.CharField(max_length=200)
    description = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class DanceBooking(models.Model):
    """
    Model for booking dance classes.

    Fields:
        - `username` (ForeignKey): User making the booking, linked to :model:`auth.User`.
        - `date_of_booking` (DateField): Date of the reservation.
        - `dance_style` (TextField): Specific dance style chosen from predefined styles.
        - `start_time` (TimeField): Start time of the reservation chosen from predefined choices.
        - `confirmed` (BooleanField): Indicates if the booking is confirmed.
        - `message` (TextField): Extra comments or questions from the user.
    """

    username = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="dance_booking"
    )
    date_of_booking = models.DateField()
    dance_style = models.TextField(choices=DANCE_STYLES)
    start_time = models.TimeField(choices=BOOKING_TIME)
    confirmed = models.BooleanField(default=False)
    message = models.TextField(max_length=500, blank=True)

    class Meta:
        ordering = ["date_of_booking", "start_time"]

    def __str__(self):
        return (
            f"{self.dance_style} class for {self.username} "
            f"on {self.date_of_booking} at {self.start_time}"
        )
