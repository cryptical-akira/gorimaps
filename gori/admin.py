from django.contrib import admin
from .models import History, Culture, Architect, AboutProjectDonors, Human, Video, PinedPost, Pin, PostForPin


admin.site.register(History)
admin.site.register(Culture)
admin.site.register(Architect)
admin.site.register(AboutProjectDonors)
admin.site.register(Human)
admin.site.register(Video)
admin.site.register(PinedPost)
admin.site.register(PostForPin)
admin.site.register(Pin)