from django.utils.html import escapejs
from jinja2 import Environment
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse

def environment(**options):
    env = Environment(**options)

    # Add Django's static and url as globals
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
    })

    # Define a custom Jinja2 filter using Django's escapejs
    def escapejs_filter(value):
        return escapejs(value)

    # Register the filter with Jinja2
    env.filters['escapejs'] = escapejs_filter

    return env
