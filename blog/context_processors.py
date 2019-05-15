from .models import Category


def common(request):
    """Data to pass for template every time."""

    context = {
        'category_list': Category.objects.all()
    }

    return context
