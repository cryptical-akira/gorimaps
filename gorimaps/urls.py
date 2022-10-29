from django.contrib import admin
from django.urls import path, include, register_converter
from gori.views import index_page, index_wout_lang, about_project, history, culture, architect, humans, videos, error_404_view
from gori.views import history_detail_view, culture_detail_view, architect_detail_view, search, text_us, humans_detail
from .converters import LanguagePathConverter


register_converter(LanguagePathConverter, 'lang')

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', index_wout_lang, name="index"),
    path('<lang:lang>/', index_page, name="index_page"),

    path('about-project/<lang:lang>/', about_project, name="about_project"),

    path('history/<lang:lang>/', history, name="history"),
    path('history/<int:id>/<lang:lang>/', history_detail_view, name='history-detail'),

    path('culture/<lang:lang>/', culture, name="culture"),
    path('culture/<int:id>/<lang:lang>/', culture_detail_view, name='culture-detail'),

    path('architect/<lang:lang>/', architect, name="architect"),
    path('architect/<int:id>/<lang:lang>/', architect_detail_view, name='architect-detail'),

    path('search/<lang:lang>/', search, name='search'),

    path('text-us/<lang:lang>/', text_us, name='text_us'),

    path('humans/<lang:lang>/', humans, name='humans'),
    path('humans/<int:id>/<lang:lang>/', humans_detail, name='humans_detail'),

    path('videos/<lang:lang>/', videos, name='videos'),

]


handler404 = error_404_view
handler500 = error_404_view