from django import template
from tweets.models import Comment

register = template.Library()

@register.filter
def get_comment(comment_id):
    try:
        return Comment.objects.get(id=comment_id)
    except Comment.DoesNotExist:
        return None
