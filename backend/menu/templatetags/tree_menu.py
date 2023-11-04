from django import template
from django.http import HttpRequest
from django.template import RequestContext
from django.urls import reverse, NoReverseMatch

from ..models import MenuItem

register = template.Library()


def get_menu_dict(context: RequestContext, name: str):
    """Создает словарь элементов меню"""
    # Сохранение текущего пути для проверки активного пункта меню
    current_path = ''
    if "request" in context and isinstance(context['request'], HttpRequest):
        current_path = context['request'].path

    # Запрос к БД
    data = MenuItem.objects.select_related().filter(root__name=name)

    # Формирование словаря в контекст ответа
    menu_dict = []
    for item in data:
        path = item.path.strip()

        # URL может быть задан либо явным образом, либо поименован
        try:
            url = reverse(path)
        except NoReverseMatch:
            url = path

        menu_dict.append({
            'id': item.pk,
            'url': url,
            'name': item.name,
            'parent': item.parent_id or 0,
            'active': True if url == current_path else False,
        })
    return menu_dict


@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context: RequestContext, name: str = '', parent: int = 0):
    """
    Рекурсивно выводит меню
    """
    if parent != 0 and 'menu_dict' in context:
        menu_dict = context['menu_dict']
        insert_nav = 'False'
    else:
        # Получение меню, если его нет в контексте
        menu_dict = get_menu_dict(context, name)
        insert_nav = 'True'
    # Выбор элементов текущего уровня для отрисовки
    current_menu = (item for item in menu_dict if 'parent' in item and item['parent'] == parent)
    return {
        'menu_dict': menu_dict,
        'current_menu': current_menu,
        'insert_nav': insert_nav
    }
