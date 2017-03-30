import random
import string
from django.conf import settings
from django.core.validators import URLValidator, ValidationError

SHORTCODE_MIN = getattr(settings, "SHORTCODE_MIN",6)

def __code_generator(size=SHORTCODE_MIN, chars=string.ascii_lowercase + string.digits):
    '''new_code = ''
    for _ in range(size):
        new_code += random.choice(chars)
    return new_code'''
    return ''.join(random.choice(chars) for _ in range(size))


def create_shortcode(instance,size=SHORTCODE_MIN):
    new_code = __code_generator()
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(shorturl=new_code).exists()
    if qs_exists:
        new_code = create_shortcode(size=size)
    return new_code


def validate_url(value):
    url_validator = URLValidator()
    try:
        url_validator(value)
    except:
        raise ValidationError("Invalid Url")
    return value