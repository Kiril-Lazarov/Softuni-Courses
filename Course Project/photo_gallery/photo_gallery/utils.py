import random
import string
from django.views import generic as views
from django.shortcuts import redirect
from django.utils.text import slugify


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_slug_generator(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)

    Klass = instance.__class__
    slug_exists = Klass.objects.filter(slug=slug).exists()
    if slug_exists:
        new_slug = f'{slug}-{random_string_generator(size=4)}'
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug


class OwnerRequired(views.UpdateView):
    def get(self, request, *args, **kwargs):
        result = super().get(request, *args, **kwargs)
        print(request.user.pk)
        print(self.object.id)
        if request.user.pk == self.object.id:
            return result
        else:
            return redirect('index')

