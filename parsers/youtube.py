from django.template import Template, Context
from django.conf import settings


def parse(kwargs):
    link = kwargs.get('link')

    if link:
        width = int(kwargs.get(
            'w',
            getattr(settings, 'SHORTCODES_YOUTUBE_WIDTH', 480))
        )
        height = int(kwargs.get(
            'h',
            getattr(settings, 'SHORTCODES_YOUTUBE_HEIGHT', 385))
        )
    
    html = '<iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" frameborder="0" width="{{width}}"  height="{{height}}" src="'+ link +'"></iframe>'

    template = Template(html)
    context = Context({
        'id': link,
        'width': width,
        'height': height
    })

    if link:
        return template.render(context)
    else:
        return '<strong>Video not found</strong>'
