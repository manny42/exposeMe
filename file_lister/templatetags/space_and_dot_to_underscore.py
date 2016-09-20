from django import template
import re

register = template.Library()


def space_and_dot_to_underscore(val):
    return re.sub(r"[ \.]", '_', val)

register.filter("space_and_dot_to_underscore", space_and_dot_to_underscore)
