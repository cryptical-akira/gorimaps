from django.db import models
from django.utils.translation import get_language, gettext_lazy as _
from django.conf import settings
from django.core.exceptions import ValidationError


class MultilanguageTextAbstract(models.Model):
    text_en = models.CharField(default='', max_length=64)
    text_ka = models.CharField(default='', max_length=64)
    # unique=True
    slug = models.SlugField(null=True, blank=True, max_length=40, 
        default='transl_slug')

#    def clean(self):
#        if self.slug and type(self).objects.filter(slug=self.slug).exclude(id=self.id).count() > 0:
#            raise ValidationError(
#                ('Slug is not uniqe'))

    def __str__(self):
        lang = get_language()
        if not lang:
            lang = 'en'
        current_lang_fieldname = f'text_{lang[:2]}'

        try:
            return getattr(self, current_lang_fieldname)
        except:
            return self.text_en

    def get_text(self, lang):
        current_lang_fieldname = f'text_{lang}'
        try:
            return getattr(self, current_lang_fieldname)
        except:
            return self.text_en

    def set_text(self, lang, text):
        current_lang_fieldname = f'text_{lang}'
        try:
            setattr(self, current_lang_fieldname, text)
        except:
            self.text_en = text
    class Meta:
        abstract = True


class MultilanguageText(MultilanguageTextAbstract):
    pass


class MultilanguageLongText(MultilanguageTextAbstract):
    text_en = models.CharField(default='', max_length=512)
    text_ka = models.CharField(default='', max_length=512)


class MultilanguageTextField(MultilanguageTextAbstract):
    text_en = models.TextField(default='',)
    text_ka = models.TextField(default='',)

    @property
    def text_en_intro(self):
        return self.text_en[:60]
    @property
    def text_ka_intro(self):
        return self.text_ka[:60]

### !!! TO BE DELETED
CHAR_TRANSL_FIELD_CHOICES = (
    ('image-title', 'image title'),
    ('image-descr', 'image description'),
    ('person-firstname', 'person first name'),
    ('person-lastname', 'person last name'),
)

FIELD_DICT = {
    'image-title': 'title',
    'image-descr': 'descr',
    'person-firstname': 'first_name',
    'person-lastname': 'last_name',
}

class CharTransl(models.Model):
    field = models.CharField(default='image-title', max_length=30,
                             choices=CHAR_TRANSL_FIELD_CHOICES)
    lang = models.CharField(default='ka', max_length=2,
                            choices=settings.SITE_LANG_CHOICES)
    val = models.CharField(max_length=500)

    def __str__(self):
        return self.val
