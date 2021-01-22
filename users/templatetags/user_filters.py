from django import template
from django.core.mail import send_mail
# в ней зарегистрированы все теги и фильтры шаблонов
# добавляем к ним и наш фильтр
register = template.Library()


@register.filter
def addclass(field, css):
    return field.as_widget(attrs={"class": css})

@register.filter
def uglify(text):
    for field in text:
        print(field)
    return "".join(c.upper() if i % 2 else c.lower() for i,c in enumerate(text))
