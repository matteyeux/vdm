from django import template
from django.template.defaultfilters import stringfilter

import datetime

register = template.Library()

# @register.filter
# @stringfilter
@register.filter(name='string_to_date')
def string_to_date(value, arg):
	date_obj = datetime.datetime.strptime(value, arg)
	new_date = date_obj.strftime('%d/%m/%Y')
	return new_date

@register.filter(name='number_to_money')
def string_to_date(value, arg):
	date_obj = datetime.datetime.strptime(value, arg)
	new_date = date_obj.strftime('%d/%m/%Y')
	return new_date

@register.simple_tag
def set_var(val=None):
	return val