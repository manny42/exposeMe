from django import template
import re

register = template.Library()


def special_to_underscore(val):
    return re.sub(r"[ \.\,\t\?\!]", '_', val)


def remove_brackets_and_plus(val):
    return re.sub(r"[()\[\]\{\}+]", '', val)


def replace_plus_in_url(val):
    return re.sub(r"\+", "%2B", val)

register.filter("special_to_underscore", special_to_underscore)
register.filter("remove_brackets_and_plus", remove_brackets_and_plus)
register.filter("replace_plus_in_url", replace_plus_in_url)
