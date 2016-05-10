from django import template

register = template.Library()

@register.assignment_tag(takes_context=True)
def device_size(context):
    """Create a variable in context containing the devices' size
    as recorded by django-responsive2
    
    Usage in template: {% device_size as device_size %}
    
    <div class="{{ device_size }}">...</div>
    """
    device = context.get('device', '')
    if device:
        li = [key for key, value in \
        device.match_media_queries().iteritems() if value]
        device = ' '.join(li)
    return device
