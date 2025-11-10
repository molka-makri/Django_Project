from django import template

register = template.Library()

@register.filter
def split(value, delimiter=","):
    """Divise une chaîne selon un délimiteur"""
    if value:
        return [item.strip() for item in str(value).split(delimiter) if item.strip()]
    return []

@register.filter
def filesizeformat(value):
    """Formate la taille de fichier en unités lisibles"""
    if value is None:
        return "0 bytes"
    
    try:
        value = float(value)
    except (TypeError, ValueError):
        return "0 bytes"
    
    if value < 1024:
        return f"{value:.1f} bytes"
    elif value < 1024 * 1024:
        return f"{value/1024:.1f} KB"
    elif value < 1024 * 1024 * 1024:
        return f"{value/(1024*1024):.1f} MB"
    else:
        return f"{value/(1024*1024*1024):.1f} GB"