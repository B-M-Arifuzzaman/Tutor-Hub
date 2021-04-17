import string
import random
from django.utils.text import slugify


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def unique_course_code_generator(instance):
    """
    This is for a Django project and it assumes your instance 
    has a model with a class_code field.
    """
    new_class_code = random_string_generator()
    
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(class_code=new_class_code).exists()
    if qs_exists:
        return unique_slug_generator(instance)
    return new_class_code

def unique_slug_generator(instance, new_slug=None):
    """
    This is for a Django project and it assumes your instance 
    has a model with a slug field and a title character (char) field.
    """
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug=slug,
            randstr=random_string_generator(size=4)
        )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug


def unique_lecture_id_generator(instance):
    """
    This is for a Django project and it assumes your instance 
    has a model with a class_code field.
    """
    new_lecture_id = random_string_generator()
    
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(lecture_id=new_lecture_id).exists()
    if qs_exists:
        return unique_slug_generator(instance)
    return new_lecture_id
    
    
    