from django.contrib import admin
from django.urls import path, include, register_converter
from gori.views import index_page, index_wout_lang, about_project, history, culture, architect
from .converters import LanguagePathConverter


register_converter(LanguagePathConverter, 'lang')

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', index_wout_lang, name="index"),
    path('<lang:lang>/', index_page, name="index_page"),

    path('about-project/<lang:lang>/', about_project, name="about_project"),

    path('history/<lang:lang>/', history, name="history"),

    path('culture/<lang:lang>/', culture, name="culture"),

    path('architect/<lang:lang>/', architect, name="architect"),
]
