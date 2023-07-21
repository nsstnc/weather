from django import template

register = template.Library()


@register.filter(name='split')
def split(value, key=' '):
    return value.split(key)


@register.filter(name='translate')
def translate(value):
    from deep_translator import GoogleTranslator

    return GoogleTranslator(source='en', target='ru').translate(value)