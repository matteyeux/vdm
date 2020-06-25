from django.shortcuts import render


def vdm_report_page(request):
   return render(request, 'order_report.html', {})