from django import template

register = template.Library()

@register.inclusion_tag('unfold/components/button.html')
def button_component(submit=False):
    return {'submit': submit}

@register.inclusion_tag('unfold/components/card.html')
def card_component(class_name, title, footer, label, icon):
    return {
        'class': class_name,
        'title': title,
        'footer': footer,
        'label': label,
        'icon': icon,
    }

@register.inclusion_tag('unfold/components/container.html')
def container_component(class_name):
    return {'class': class_name}

@register.inclusion_tag('unfold/components/flex.html')
def flex_component(class_name, col=False):
    return {'class': class_name, 'col': col}

@register.inclusion_tag('unfold/components/icon.html')
def icon_component(class_name):
    return {'class': class_name}

@register.inclusion_tag('unfold/components/navigation.html')
def navigation_component(class_name, items):
    return {'class': class_name, 'items': items}

@register.inclusion_tag('unfold/components/progress.html')
def progress_component(class_name, value, title, description):
    return {'class': class_name, 'value': value, 'title': title, 'description': description}

@register.inclusion_tag('unfold/components/separator.html')
def separator_component(class_name):
    return {'class': class_name}

@register.inclusion_tag('unfold/components/table.html')
def table_component(table, card_included=False, striped=False):
    return {'table': table, 'card_included': card_included, 'striped': striped}

@register.inclusion_tag('unfold/components/text.html')
def text_component(class_name):
    return {'class': class_name}

@register.inclusion_tag('unfold/components/title.html')
def title_component(class_name):
    return {'class': class_name}