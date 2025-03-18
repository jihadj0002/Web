# pdfread/templatetags/custom_filters.py
import base64
from django import template

register = template.Library()

@register.filter
def base64_encode(data):
    """
    Encode binary data as Base64.
    """
    return base64.b64encode(data).decode('utf-8')