from django import template

# Bookmark
register = template.Library()  # register decorator


@register.filter(name='is_bookmarked')
def is_bookmarked(donor, bookmarks):
    for bookmark in bookmarks:
        if(bookmark.donor.user.id == donor.user.id):
            return True

    return False
