from django.conf import settings
from django.utils.translation import activate


class LanguagePathConverter:
    regex = '[^/]+'

    def to_python(self, value):
        # convert value to its corresponding python datatype
        activate(value)
        return value

    def to_url(self, value):
        # convert the value to str data
        return value
