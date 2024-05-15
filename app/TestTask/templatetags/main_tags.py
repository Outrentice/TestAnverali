from django import template
import locale

register = template.Library()


@register.simple_tag()
def get_date_joined(date):
    locale.setlocale(
        category=locale.LC_ALL,
        locale="Russian"
    )
    if date.strftime("%d.%m.%Y") == date.today().strftime("%d.%m.%Y"):
        return "Сегодня"

    return date.strftime('%B %Y'), date.today().strftime("%d.%m.%Y"), date.strftime("%d.%m.%Y")
