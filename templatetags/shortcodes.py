from website.apps.shortcodes import parser
from django import template
register = template.Library()


def shortcodes_replace(value):
    print(value)
    return parser.parse(value)

register.filter('shortcodes', shortcodes_replace)
