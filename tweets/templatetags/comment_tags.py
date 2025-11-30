from django import template

register = template.Library()

@register.inclusion_tag('tweets/comment_item.html', takes_context=True)
def render_comment(context, comment):
    return {
        'comment': comment,
        'user': context.get('user'),
    }
