from django.template import Template, Context
from django.conf import settings


def parse(kwargs):
    src = kwargs.get('src')
    
    html = '<img class="post-content-image" src="'+ src +'">'

    template = Template(html)
    context = Context({
        'id': src
    })

    if src:
        return template.render(context)
    else:
        return 'Image not found'
