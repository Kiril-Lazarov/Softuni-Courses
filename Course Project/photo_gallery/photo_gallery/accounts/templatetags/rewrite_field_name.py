from django.template import Library

register = Library()


@register.filter('rewrite_field_name')
def rewrite_field_name(value):
    value = value.replace('_', ' ')
    value = value[0].upper() + value[1:]
    return value
