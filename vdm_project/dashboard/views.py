from django.shortcuts import render


def vdm_report_page(request):
    return render(request, 'order_report.html', {})

def vdm_list_booking_page(request):
    bookings_data = Booking.object.all()
    return render(request, 'list_booking.html', {})