from django import template

from transl.models import MultilanguageText, MultilanguageLongText, MultilanguageTextField

register = template.Library()

'''@register.simple_tag
def mlcf(tobj, tfield, lang):   #multilingual charfield
    if lang == 'en':
        return getattr(tobj, FIELD_DICT[tfield])
    else:
        ttransl = tobj.transl.all().filter(field=tfield, lang=lang).first()
        return ttransl.val if ttransl else '''

@register.simple_tag
def t(tslug):
    try:
        tobj = MultilanguageTextField.objects.get(slug=tslug)
        return tobj.__str__()
    except:
        try:
            tobj = MultilanguageText.objects.get(slug=tslug)
            return tobj.__str__()
        except:
            return ''

