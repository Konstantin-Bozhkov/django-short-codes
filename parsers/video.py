from django.template import Template, Context
from django.conf import settings


def parse(kwargs):
    src = kwargs.get('src')
    
    html = '<video class="post-video">'
    html += '<source src="{{src}}" type="video/mp4>'
    html += '</source>'
    
    template = Template(html)
    context = Context({
        'id': src
    })
    if src:
        return template.render(context)
    else:
        return '<strong>Video not found</strong>'
