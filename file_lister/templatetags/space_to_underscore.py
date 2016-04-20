from django import template

register = template.Library()

def space_to_underscore(val):
	return val.replace(' ', '_')

register.filter('space_to_underscore', space_to_underscore)