from django import template
from datetime import datetime

register = template.Library()

@register.filter
def timestamp_to_date(value):
    try:
        timestamp = int(value)
        date = datetime.fromtimestamp(timestamp)
        return date.strftime("%d %b %Y")
    except (ValueError, TypeError):
        return value


@register.filter
def truncate_text(value, length):
    if len(value) > length:
        return value[:length] + '...'
    else:
        return value
