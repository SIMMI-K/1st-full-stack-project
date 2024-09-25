from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views.generic import UpdateView, DeleteView
from django.contrib import messages
from .models import DanceBooking
from .forms import DanceBookingForm

# Views

@login_required
def booking_view(request):
    """
    Renders the Dance Booking page where users can view and book dance classes.

    **Context**

    ``bookings``
        All bookings made by the current user, ordered by date and time
        from :model:`booking.DanceBooking`
    ``booking_form``
        An instance of :form:`booking.DanceBookingForm` for submitting
        booking requests.

    **Template**
        :template:`booking/booking.html`
    """
    if request.method == "POST":
        booking_form = DanceBookingForm(data=request.POST)
        if booking_form.is_valid():
            bookings = booking_form.save(commit=False)
            bookings.username = request.user
            bookings.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Booking submitted! You will be notified once confirmed.",
            )
            return HttpResponseRedirect(reverse("booking"))
    else:
        booking_form = DanceBookingForm()

    bookings = (
        DanceBooking.objects.filter(username=request.user)
        .order_by("date_of_booking", "start_time")
    )

    return render(
        request,
        "booking/booking.html",
        {
            "bookings": bookings,
            "booking_form": booking_form,
        },
    )


class EditDanceBooking(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Allows users to edit their dance class bookings.

    **Context**

    ``booking``
        Represents the booking instance to be edited

     **Template**

    :template:`booking/edit_dance_booking.html`
    """

    model = DanceBooking
    template_name = "booking/edit_dance_booking.html"
    form_class = DanceBookingForm
    success_url = "/booking/"

    def form_valid(self, form):
        form.instance.confirmed = False  # Reset confirmation on edit
        messages.success(
            self.request,
            "Your booking has been updated!",
            extra_tags="alert alert-success alert-dismissible",
        )
        return super().form_valid(form)

    def test_func(self):
        """
        Ensure that only the owner of the booking can edit it.

        Returns:
            bool: True if the logged in user is the owner of the booking, False otherwise.
        """
        booking = self.get_object()
        return (self.request.user == booking.username or self.request.user.is_superuser)


class DeleteDanceBooking(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Allows users to delete their dance class bookings.

    **Context**

    ``booking``
        Represents the booking instance to be deleted.

    **Template**

    :template:`booking/booking_confirm_delete.html`
    """

    model = DanceBooking
    success_url = "/booking/"

    def form_valid(self, form):
        messages.success(
            self.request,
            "Your booking has been deleted successfully!",
            extra_tags="alert alert-success alert-dismissible",
        )
        return super().form_valid(form)

    def test_func(self):
        """
        Ensure that only the owner of the booking can delete it.

        Returns:
            bool: True if the logged in user is the owner of the booking, False otherwise.
        """
        booking = self.get_object()
        return (self.request.user == booking.username or self.request.user.is_superuser)
