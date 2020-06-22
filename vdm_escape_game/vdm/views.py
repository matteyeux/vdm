from django.http import JsonResponse
from django.shortcuts import render
from vdm.models import order
from django.core import serializer

def vdm_with_pivot(request):
	return render(request, 'vdm_with_pivot.html', {})

def pivot_date(request):
	dataset = Order.objects.all()
	data = serilizers.serialize('json', dataset)
	return JsonResponse(data, safe=False)